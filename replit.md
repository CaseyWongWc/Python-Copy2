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

  - `# in: <value>` comments
        build a queue feeding `input()` calls in source order. Real stdin is
        used once the queue is empty. Old `# setin` directives still work and
        feed the same queue.

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
