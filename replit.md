# ZyBooks Inline-Output Tools

Casey's Replit project for working through ZyBooks Python exercises with
Jupyter-style inline annotations. Each line of code that prints or has a bare
expression value gets a `# out:` or `# val:` comment appended to it after the
file is run.

## Layout

```
.
├── inline_output_v4.py      ← root annotator (`main.py` uses this)
├── inline_output_v5.py      ← deprecated marker-based experiment
├── main.py                  ← runs v4 on goog.py at the project root
├── goog.py                  ← root working file (long-form ZyBooks notes)
├── Helpers/helpings.py      ← INFO(), setin(), ret_file(), quiz(), etc.
├── old/                     ← prior versions kept for reference
└── sandbox/                 ← v6 "magic with" notebook (self-contained)
    ├── notebook/
    │   ├── main.py          ← click Run -> annotates goog.py here
    │   └── goog.py          ← starter / cheat sheet for v6
    ├── files/               ← default home for `with "name.txt":` files
    └── inline_output_v6.py  ← v4 + magic `with` blocks + `# in:` queue
```

## v4 (root)

`python main.py` annotates `goog.py` in place. Magic save comments on the
first 5 lines of the file copy the annotated file somewhere useful:

  - `# zy: 12.1 Item_Produce`  -> `_zybooks/C_12/12.1/Item_Produce.py`
  - `# fig: 12.1.1`            -> `_zybooks/C_12/Figure_12_1_1.py`
  - `# quick: name`            -> `scratch/name.py`
  - `# note: name`             -> `notes/name.md`
  - `# save: any/path/here.py` -> exact path

`STRIP_AFTER_SAVE` toggle in `main.py` controls whether annotations stay in
`goog.py` after the auto-save (default: stay).

## v6 (sandbox/)

Self-contained "notebook" version. Run via `python sandbox/notebook/main.py`
(or just click Run from the workspace inside that file). Adds three preprocessor
features Casey actually uses:

  - `with "filename.ext":`  body becomes that file's raw contents
        - any relative path (`"in.txt"`, `"sub/in.txt"`) -> resolved
          inside `sandbox/files/`
        - absolute path (`"/tmp/x"`, `"C:\\..."`) -> exact path
        - body does NOT have to be valid Python
        - `main.py` chdirs into `sandbox/files/` before running, so
          `open("name.txt")` reads from the EXACT same place
          `with "name.txt":` writes to — no `../files/` dance.

  - `with Scratch:` (or `with _:` / `with __:`)
        body runs as Python and gets annotated, but every variable assigned
        inside is reverted when the block ends. `with Scratch as a:` captures
        each variable onto `a` so `a.x`, `a.y`, ... live on after the block.

  - `with "X" as Scratch:` (and friends)
        Combined "save the body to disk AND run it sandboxed" form, fusing
        the two-step `with "X":` + `with Scratch:` pattern Casey kept
        retyping. The body lands on disk verbatim at the resolved path
        (same path rules as `with "X":`) AND runs in-process with normal
        Scratch isolation. Body annotations work normally (`# out:` for
        `print`, `# val:` for bare expressions). Five header shapes are
        accepted, all interchangeable:
          `with "name.py" as Scratch:`
          `with "name.py" as Scratch as h:`        (capture locals on `h`)
          `with "name.py", Scratch:` /
              `with "name.py", Scratch as h:`      (Python's native
                                                   multi-context-manager
                                                   comma syntax)
          `with Scratch: "name.py"` /
              `with Scratch as h: "name.py"`       (reversed shape — same
                                                   semantics, just easier
                                                   to type when editing on
                                                   phone where the Scratch
                                                   keyword sits at the
                                                   front of the line)
        If the body is not valid Python the file is NOT written, the
        header gets a `# !err: SyntaxError ...` annotation, and the body
        is blanked so the rest of the notebook still parses and gets
        annotated. The save-and-run is in-process — for fresh-subprocess
        isolation use a separate `with RUN:` block.

        Clean-save: the file written to disk has notebook-only annotation
        lines stripped (`# in:`, `# out:`, `# val:`, `# !err:`, `# err:`)
        and runs of 3+ blank lines collapsed to one blank. So iterating
        on a save+run block doesn't grow the saved file taller every
        run; what lands on disk is always a clean, runnable script.

        Capture (`as h:`): when a capture variable is bound, the namespace
        object also exposes `h.out` (list of printed lines, one entry per
        newline-split piece), `h.outs` (`'\n'.join(h.out)` for one-liner
        round-trips with `print(h.outs)`), and `h.err` (list of stderr
        lines, captured via a tee on `sys.stderr.write`). These attrs
        live alongside the body's locals, so `h.x` and `h.out` coexist.
        `with Scratch:` (no `as`) skips capture — nothing reads it, so
        the wrapper isn't installed.

  - `# in: <value>` comments
        build a queue feeding `input()` calls in source order. Real stdin is
        used once the queue is empty. Old `# setin` directives still work and
        feed the same queue.

  - `with bash:`
        each indented body line is one shell command, run via `/bin/sh -c`
        from `sandbox/files/` AFTER the Python notebook finishes (so files
        written from Python are visible to the shell). Each command's stdout
        becomes `# out:` annotations on the line, stderr becomes `# err:`
        (lowercase, distinct from `# !err:`), and a non-zero exit appends
        `# !err: exit code N`. Blank/comment lines in the body are preserved
        and ignored. A failing command does NOT abort the rest of the
        notebook. Default 30s per-command timeout (no knob to tweak).
        Linux/macOS only — `/bin/sh` is required.

  - `with RUN:` (and `with RUN: <args>`)
        the indented body is dedented, written to a uniquely-named temp
        file under `sandbox/files/.run_blocks/`, and run in a brand-new
        `python3` subprocess from `sandbox/files/`. This is FULL process
        isolation, not just namespace isolation like `Scratch` — globals
        from the surrounding notebook are invisible inside, `sys.modules`
        is empty, and `# in:` queues from the outer notebook are not
        shared. Optional inline args (`with RUN: -O`, `with RUN: -V`,
        `with RUN: --foo bar`) are shell-split (`shlex`) and passed to
        `python3` before the temp file. After the run, all stdout lines
        become `# out:` under the LAST non-blank body line, stderr lines
        become `# err:` there too, and a non-zero exit appends
        `# !err: subprocess exited with code N`. Temp files are deleted
        on success and KEPT on failure for debugging. No timeout — Casey
        can ctrl-C. Use this whenever the body needs `import main` to
        re-import fresh, or anything else where leftover notebook state
        would muddy the result.

        Stdin is ALWAYS a closed pipe (even when the body has no
        `# in:` directives), so an `input()` call that runs past the
        queue raises EOFError immediately instead of blocking on the
        parent's real stdin. That EOFError surfaces as a normal
        `# err:` traceback annotation plus the non-zero exit line — no
        more invisible hangs that need a ctrl-C to recover from.

  - `with "X" as RUN:` (and `with "X", RUN:`, with optional inline argv)
        Combined "save the body to disk AND run it in a fresh python3
        subprocess" form. Fuses the two-step `with "X":` + `with RUN:`
        pattern Casey kept retyping when iterating on a script he wanted
        both saved AND executed with full process isolation. The body
        lands on disk verbatim at the resolved path (same path rules as
        `with "X":`) AND is queued through the same subprocess machinery
        as plain `with RUN:`. All RUN behaviors carry over: stdout/stderr
        land as `# out:` / `# err:` under the LAST non-blank body line,
        non-zero exit appends `# !err: subprocess exited with code N`,
        inline argv works (`with "X" as RUN: -O`, `with "X", RUN: -V`),
        the body's own `# in:` directives feed the subprocess's stdin,
        and the outer notebook's `# in:` queue is NOT shared. Three
        header shapes are accepted, all interchangeable:
          `with "name.py" as RUN:`
          `with "name.py" as RUN: -O`               (inline python3 argv)
          `with "name.py", RUN:` /
              `with "name.py", RUN: --foo bar`      (Python's native
                                                    multi-context-manager
                                                    comma syntax)
        If the body is not valid Python the file is NOT written, the
        subprocess is NOT queued, and the header gets a
        `# !err: SyntaxError ...` annotation. The body is blanked so the
        rest of the notebook still parses and gets annotated (mirrors
        `with "X" as Scratch:`). Stronger isolation than `with "X" as
        Scratch:` (that one is in-process namespace isolation only).

        Clean-save: same as `with "X" as Scratch:` — the file written
        to disk has notebook annotation lines (`# in:` / `# out:` /
        `# val:` / `# !err:` / `# err:`) stripped and triple-blank
        runs collapsed to one blank, so the saved file stays a clean
        runnable script across iterations. The subprocess still sees
        the ORIGINAL body text via the in-memory queue, so the body's
        own `# in:` directives still feed its stdin — only the file
        on disk is cleaned.

All v4 features (`# out:` / `# val:` / `# !err:` / magic save comments / v4
string-splitting fix) carry over.

## User notes

- Casey edits on phone often, so keep formatting predictable and avoid huge
  reflows.
- Pasted ZyBooks problem statements can be huge docstrings — the v6
  preprocessor uses Python's `tokenize` module to find REAL `with`
  statements, so identical-looking text inside triple-quoted docstrings
  is left completely alone (no file extraction, no scope rewriting).
  Known tradeoff: if the source can't be tokenized at all (e.g.
  intentionally malformed bytes from a paste accident), v6 falls back
  to permissive line-regex matching so the magic features still work
  — at the small cost that a magic-looking line inside a docstring in
  that broken file might trigger preprocessing. In practice this is
  vanishingly rare since Casey's notebooks tokenize fine.
- `sandbox/files/` is a runtime output directory: only `.gitkeep` and
  `.gitignore` are tracked, every other file (e.g. `names.txt` written
  by `with "names.txt":`) is regenerated on each run and ignored by
  git.
- The sandbox folder is intentionally isolated from the root v3/v4/v5 setup;
  experimenting in `sandbox/notebook/goog.py` cannot break the root tools.
- An "empty" `with Scratch:` (or `with _:` / `with __:` / `... as a:`)
  block is fine — v6 quietly emits `with __nb_Scratch__(): pass` so the
  notebook still parses and the rest of the file gets annotated. The
  same is true when a Scratch block's only body is one or more
  `with "X":` blocks (those get extracted to disk first, leaving the
  Scratch block effectively empty — v6 handles that too).
- `sandbox/files/` is on `sys.path` inside the notebook run (prepended
  at the front), so a `with "helper.py":` block followed by
  `import helper` in the same file Just Works. Each notebook run is a
  fresh subprocess, so module re-imports always pick up the latest
  source — no stale-cache surprises after editing the helper.
  Subdirectories work too: writing `with "pkg/util.py":` auto-creates
  an empty `pkg/__init__.py` (existing `__init__.py` files are never
  overwritten) so `from pkg import util` resolves cleanly.
- `sandbox/notebook/` is ALSO on `sys.path` inside the run (right after
  `sandbox/files/`), so any sibling package next to `goog.py` is
  importable. Drop `sandbox/notebook/Helpers/helpings.py` next to the
  notebook and `from Helpers.helpings import *` works the same way it
  did from the project root in the v4 setup. `with RUN:` subprocesses
  inherit both directories via PYTHONPATH so imports work identically
  in fresh-process mode too.
- The Run button is wired to `python sandbox/notebook/main.py` (the v6
  sandbox runner), not the v3/v4 root files. Run from the shell to
  exercise v4: `python main.py` (still works, untouched).
- Heads-up on `with "X":` body content: it is RAW TEXT. Do NOT wrap the
  body in `'''...'''` thinking it needs to be a Python string literal.
  Wrapping markdown in triple quotes inside a `with "README.MD":` block
  leaves a stray closing `'''` outside the indented body, which Python
  reads as an open string literal that swallows the rest of `goog.py`
  and produces a confusing "unterminated triple-quoted string" error
  far below where the actual problem lives.
- Phone-friendly indentation handling (added on top of v6):
  1. `_normalize_whitespace` runs BEFORE the preprocessor — leading TAB
     characters become 4 spaces, leading non-breaking spaces (U+00A0)
     become regular spaces. Only LEADING whitespace is touched, and
     `tokenize` is used to skip lines that live inside multi-line string
     literals so string contents stay byte-exact (a tab in `print("a\\tb")`
     or inside a triple-quoted string is never mangled). On tokenize
     failure (already broken source) we normalize every line — usually
     fixing the very thing that made tokenize fail.
  2. After preprocessing, `run_and_annotate` does an `ast.parse` pre-flight
     on the runnable source. An `IndentationError` becomes a 1–3 line
     `# !err:` annotation that names the bad line AND the previous line,
     reports both indent counts, and (for "expected indented block")
     suggests a target indent. A `SyntaxError` becomes a one-line
     `# !err: SyntaxError on line N: ...` instead of a raw multi-line
     traceback. The shim subprocess is skipped entirely when pre-flight
     fails — no point running broken Python.
- `with "X":` bodies have always been dedented before being written to
  disk (smallest non-blank body indent is the dedent base). So a
  `with "README.MD":` block at indent 0 with body at indent 4 produces
  a clean README starting at column 0, not column 4.
