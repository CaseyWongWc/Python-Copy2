"""
inline_output_v6.py
Casey's sandbox notebook — v4 + magic `with` blocks + `# in:` inputs.

What's NEW in v6 (on top of v4):

1.  `with "filename.ext":`
        The indented block becomes the file's CONTENTS (raw text, dedented).
    Optional setting `sandbox.sameLevelRawWithBlocks = true` also lets
    a same-level triple-quoted body be treated as verbatim raw text.
        The block does NOT have to be valid Python.
        Bare name (e.g. "input.txt") -> goes to <sandbox>/files/<name>.
        Path containing /            -> relative to the notebook directory.
        Absolute path                -> exact path.

2.  `with Scratch:`  (or `with _:` / `with __:`)
        The indented block runs as Python and gets the normal annotations,
        but every variable assigned inside DISAPPEARS after the block ends.

3.  `with Scratch as a:` (or `with _ as a:` / `with __ as a:`)
        Same isolation, but each variable defined inside is captured onto `a`.
        After the block, `a.x`, `a.y`, ... are available.

4.  `# in: <value>` comments anywhere in the file
        Build a queue that feeds `input()` calls in source order.
        (Old `# setin` directives still work and feed the same queue.)
        Once the queue is empty, real stdin is used.

5.  `with bash:`
        The indented block is a list of shell commands (one per line),
        each run via `/bin/sh -c` from `sandbox/files/`. After the run,
        each command line is annotated:
          stdout      -> `# out:`
          stderr      -> `# err:`     (lowercase)
          non-zero rc -> `# !err: exit code N`
        Blank lines and `#` comments inside the body are preserved and
        ignored. A failing command does NOT abort the rest of the notebook.

Everything else from v4 still applies:
  -  print()                       -> `# out:`
  -  bare expressions              -> `# val:`  (with v4 string-splitting fix)
  -  errors                        -> `# !err:`
  -  # zy: / # fig: / # quick: / # note: / # save: magic auto-save
"""

import ast
import io
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tokenize
import uuid
from pathlib import Path

OUT_PREFIX = "# out:"
VAL_PREFIX = "# val:"
ERR_PREFIX = "# !err:"
BASH_ERR_PREFIX = "# err:"
SAME_LEVEL_RAW_WITH_SETTING = "sandbox.sameLevelRawWithBlocks"


# ---------- magic comment parsing (auto-save) ----------

def _parse_magic(src: str):
    """Look at the first 5 non-blank lines for a magic save comment."""
    lines = src.splitlines()
    checked = 0
    for line in lines:
        if checked >= 5:
            break
        stripped = line.strip()
        if not stripped:
            continue
        checked += 1

        m = re.match(r"#\s*zy:\s*(\d+)\.(\d+)\s+(\S+)", stripped)
        if m:
            chap, sub, name = m.group(1), m.group(2), m.group(3)
            return Path(f"_zybooks/C_{chap}/{chap}.{sub}/{name}.py")

        m = re.match(r"#\s*fig:\s*(\d+)\.(\d+)\.(\d+)", stripped)
        if m:
            chap, sub, num = m.group(1), m.group(2), m.group(3)
            return Path(f"_zybooks/C_{chap}/Figure_{chap}_{sub}_{num}.py")

        m = re.match(r"#\s*quick:\s*(\S+)", stripped)
        if m:
            name = m.group(1)
            if not name.endswith((".py", ".md", ".txt")):
                name += ".py"
            return Path(f"scratch/{name}")

        m = re.match(r"#\s*note:\s*(\S+)", stripped)
        if m:
            name = m.group(1)
            if not name.endswith((".md", ".txt")):
                name += ".md"
            return Path(f"notes/{name}")

        m = re.match(r"#\s*save:\s*(\S+)", stripped)
        if m:
            return Path(m.group(1))

    return None


def _auto_save(src_path: Path):
    """If the source file has a magic comment, copy the (annotated) file there."""
    src = src_path.read_text()
    dest = _parse_magic(src)
    if dest is None:
        return None
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_path, dest)
    return str(dest)


# ---------- annotation strip ----------

def _strip_old_annotations(src: str) -> str:
    keep = []
    for line in src.splitlines(keepends=True):
        stripped = line.lstrip()
        # Order matters: ERR_PREFIX (`# !err:`) must be checked before
        # BASH_ERR_PREFIX (`# err:`) is even possible to confuse — they
        # are distinct prefixes, but both start with `# ` so we just
        # check each independently.
        if (
            stripped.startswith(OUT_PREFIX)
            or stripped.startswith(VAL_PREFIX)
            or stripped.startswith(ERR_PREFIX)
            or stripped.startswith(BASH_ERR_PREFIX)
        ):
            continue
        keep.append(line)
    return "".join(keep)


_CLEAN_SAVE_IN_RE = re.compile(r"^\s*#\s*in:\s")


def _strip_for_clean_save(src: str) -> str:
    """Strip notebook-only annotation lines from a save+run body before
    writing it to disk: `# in:`, `# out:`, `# val:`, `# !err:`, and the
    `# err:` (lowercase) bash-style stderr annotation.

    Then collapse runs of 3+ blank lines down to 2 so iterated saves
    don't grow taller and taller. The saved file is meant to be a
    standalone, shareable script — not a notebook with stale scaffolding.
    """
    keep = []
    for line in src.splitlines(keepends=True):
        stripped = line.lstrip()
        if (
            stripped.startswith(OUT_PREFIX)
            or stripped.startswith(VAL_PREFIX)
            or stripped.startswith(ERR_PREFIX)
            or stripped.startswith(BASH_ERR_PREFIX)
            or _CLEAN_SAVE_IN_RE.match(line)
        ):
            continue
        keep.append(line)
    result = "".join(keep)
    # Collapse 3+ consecutive newlines to exactly 2 (one blank line).
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result


def _find_workspace_settings(start_dir: Path):
    """Return the nearest workspace settings.json path, if present."""
    for parent in (start_dir, *start_dir.parents):
        candidate = parent / ".vscode" / "settings.json"
        if candidate.exists():
            return candidate
    return None


def _read_bool_workspace_setting(start_dir: Path, key: str, default: bool) -> bool:
    """Read a boolean workspace setting, falling back cleanly on any error."""
    settings_path = _find_workspace_settings(start_dir)
    if settings_path is None:
        return default
    try:
        data = json.loads(settings_path.read_text())
    except Exception:
        return default
    value = data.get(key, default)
    return value if isinstance(value, bool) else default


# ---------- whitespace normalization ----------

def _normalize_whitespace(src: str) -> str:
    """Quietly fix the most common phone-typing whitespace mistakes:
        - leading TAB characters become 4 spaces (standard Python indent)
        - leading non-breaking spaces (U+00A0) become regular spaces
    Only the LEADING whitespace of each line is touched, so a real `\\t`
    inside a string literal (e.g. `print("a\\tb")`) is never disturbed.
    Lines whose leading whitespace is part of a multi-line string literal
    are also skipped — `tokenize` is used to find those line ranges so
    the string contents stay byte-exact. If the source can't even be
    tokenized (already broken), we normalize every line — usually the
    very thing that fixes the tokenize failure on the next pass.
    """
    if "\t" not in src and "\u00a0" not in src:
        return src

    lines = src.splitlines(keepends=True)
    skip_lines: set = set()
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
        for t in toks:
            if t.type != tokenize.STRING:
                continue
            start_line, end_line = t.start[0], t.end[0]
            # The opening line's leading whitespace is CODE (the indent
            # of the assignment statement), not string content — leave it
            # alone. Lines AFTER the opener are string body, including
            # the closing line whose leading whitespace IS part of the
            # string up until the closing quote.
            for ln in range(start_line + 1, end_line + 1):
                skip_lines.add(ln)
    except (tokenize.TokenError, IndentationError, SyntaxError):
        skip_lines = set()

    LEADING_WS_RE = re.compile(r"^[ \t\u00a0]*")
    out = []
    for i, line in enumerate(lines, start=1):
        if i in skip_lines:
            out.append(line)
            continue
        m = LEADING_WS_RE.match(line)
        if not m:
            out.append(line)
            continue
        leading = m.group(0)
        if "\t" not in leading and "\u00a0" not in leading:
            out.append(line)
            continue
        normalized = leading.replace("\t", "    ").replace("\u00a0", " ")
        out.append(normalized + line[len(leading):])
    return "".join(out)


# ---------- v6 preprocessor: magic `with` blocks ----------

WITH_STR_RE = re.compile(r'^(\s*)with\s+(["\'])(.+?)\2\s*:\s*$')
WITH_SCRATCH_RE = re.compile(
    r'^(\s*)with\s+(Scratch|__|_)(\s+as\s+\w+)?\s*:\s*$'
)
# Combined save-and-run header: `with "X" as Scratch:`,
# `with "X" as Scratch as h:`, `with "X", Scratch:` and
# `with "X", Scratch as h:`. Group meanings:
#   1: indent
#   2: open quote (closing must match — handled by \2)
#   3: path string
#   4: scratch name from the ` as Scratch` form (None for comma form)
#   5: scratch name from the `, Scratch` form (None for `as` form)
#   6: optional capture variable (e.g. `h` in `as Scratch as h:`)
WITH_SAVE_RUN_RE = re.compile(
    r'^(\s*)with\s+'
    r'(["\'])(.+?)\2'
    r'(?:\s+as\s+(Scratch|__|_)|\s*,\s*(Scratch|__|_))'
    r'(?:\s+as\s+(\w+))?'
    r'\s*:\s*$'
)
# Reversed save-and-run shape: `with Scratch: "name.py"`,
# `with Scratch as a: "name.py"`, plus `_` / `__` aliases. Same
# semantics as `with "name.py" as Scratch:` — body is the indented
# block BELOW the header (the inline string is just the path target,
# even though Python would otherwise parse it as the body). A trailing
# `:` after the string is tolerated for users who instinctively type
# one. Group meanings:
#   1: indent
#   2: scratch name (Scratch / _ / __)
#   3: optional capture variable (e.g. `a` in `as a`)
#   4: open quote (closing must match — handled by \4)
#   5: path string
WITH_SCRATCH_SAVE_RE = re.compile(
    r'^(\s*)with\s+(Scratch|__|_)(?:\s+as\s+(\w+))?\s*:\s*'
    r'(["\'])(.+?)\4\s*:?\s*$'
)
WITH_BASH_RE = re.compile(r'^(\s*)with\s+bash\s*:\s*$')
# `with RUN:` and `with RUN: <args>` (e.g. `with RUN: -O`,
# `with RUN: --foo bar`). The args portion is intentionally untyped
# (treated as a shell-style argv) and may not be valid Python — see
# _find_magic_with_lines for the sanitization step that keeps the rest
# of the file tokenizable.
WITH_RUN_RE = re.compile(r'^(\s*)with\s+RUN\s*:\s*(.*?)\s*$')
# Combined save-and-fresh-subprocess-run header:
# `with "X" as RUN:`, `with "X" as RUN: <args>`,
# `with "X", RUN:`, and `with "X", RUN: <args>`.
# Group meanings:
#   1: indent
#   2: open quote (closing must match — handled by \2)
#   3: path string
#   4: separator between path and `RUN` (` as RUN` or `, RUN`)
#   5: optional shell-style argv tail (e.g. `-O`, `--foo bar`)
# The argv portion is sanitized away before tokenize, same as plain
# `with RUN:`, so docstring isolation isn't broken when the body has
# non-Python flag syntax in the header.
WITH_SAVE_RUN_RUN_RE = re.compile(
    r'^(\s*)with\s+(["\'])(.+?)\2'
    r'(\s+as\s+RUN|\s*,\s*RUN)'
    r'\s*:\s*(.*?)\s*$'
)
RAW_TEXT_MARKERS = {"\"\"\"", "'''"}


def _find_magic_with_lines(src: str):
    """
    Tokenize the source and return four sets + two dicts keyed by 1-based
    line numbers, marking REAL magic `with` statements:
      - str_lines:     `with "X":`              (file-extraction form)
      - scratch_lines: `with Scratch:` etc.     (sandbox-scope form)
      - bash_lines:    `with bash:`             (shell-command form)
      - run_lines:     `with RUN:`              (fresh-subprocess form)
      - save_run_info: {line: (path, capture)}  (combined save-and-run
                       form: `with "X" as Scratch:`,
                       `with "X" as Scratch as h:`, `with "X", Scratch:`,
                       and `with "X", Scratch as h:`. `capture` is the
                       optional `as <name>` binding for the locals dict,
                       or None when omitted.)
      - save_run_run_info: {line: (path, argv)} (combined save-and-fresh-
                       subprocess-run form: `with "X" as RUN:`,
                       `with "X" as RUN: <args>`, `with "X", RUN:`, and
                       `with "X", RUN: <args>`. `argv` is the shell-split
                       list of tokens after the colon, passed to `python3`
                       before the temp file at run time.)

    Patterns inside docstrings or other string literals are NOT included
    because the tokenizer reports them as part of a STRING token, not as
    a `with` keyword.

    On tokenize failure, falls back to permissive matching (every line
    that looks like the pattern), so users still get magic behavior even
    when their file has unrelated tokenize-incompatible content. The
    tradeoff (rare false positive in a docstring) is preferable to
    silently disabling the feature.
    """
    str_lines: set = set()
    scratch_lines: set = set()
    bash_lines: set = set()
    run_lines: set = set()
    save_run_info: dict = {}
    save_run_run_info: dict = {}

    src_lines = src.splitlines()

    # Sanitize `with RUN: <args>` AND `with "X" as RUN: <args>` /
    # `with "X", RUN: <args>` headers down to their bare-colon form for
    # the tokenizer pass. The args (e.g. `-O`, `--foo bar`) are a
    # shell-style argv, not valid Python, and would otherwise make the
    # tokenizer (or any follow-up parse) choke — taking out docstring
    # isolation with them. Stripping happens line-by-line so docstring
    # contents that *look* like these headers remain inside their STRING
    # tokens, just with shorter text — the tokenizer still classifies
    # them as part of the string and our token walk skips them.
    sanitized_lines = []
    for line in src.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        ending = "\n" if line.endswith("\n") else ""
        m_sr_run = WITH_SAVE_RUN_RUN_RE.match(stripped)
        if m_sr_run and m_sr_run.group(5):
            indent = m_sr_run.group(1)
            quote = m_sr_run.group(2)
            path = m_sr_run.group(3)
            sep = m_sr_run.group(4)
            sanitized_lines.append(
                f"{indent}with {quote}{path}{quote}{sep}:{ending}"
            )
            continue
        m = WITH_RUN_RE.match(stripped)
        if m and m.group(2):
            indent = m.group(1)
            sanitized_lines.append(f"{indent}with RUN:{ending}")
            continue
        sanitized_lines.append(line)
    sanitized_src = "".join(sanitized_lines)

    def _argv_for_save_run_run(line_idx_1based: int):
        """Re-read the original line to recover the `with "X" as RUN: <args>`
        argv tail (sanitization stripped it before tokenize). Returns [] for
        the bare-colon form or unmatched lines (defensive)."""
        line_text = (
            src_lines[line_idx_1based - 1]
            if 0 < line_idx_1based <= len(src_lines) else ""
        )
        m = WITH_SAVE_RUN_RUN_RE.match(line_text)
        if not m:
            return []
        args_str = m.group(5) or ""
        if not args_str:
            return []
        try:
            return shlex.split(args_str)
        except ValueError:
            # Malformed quoting — treat as no args rather than crashing
            # the whole notebook run.
            return []

    try:
        toks = list(tokenize.generate_tokens(io.StringIO(sanitized_src).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        for ln_idx, line in enumerate(src.splitlines(), start=1):
            stripped_line = line.rstrip("\n")
            m_srr = WITH_SAVE_RUN_RUN_RE.match(stripped_line)
            if m_srr:
                # Save+RUN takes precedence over plain `with "X":` and
                # plain `with RUN:` so the same line never lands in two
                # passes.
                path = m_srr.group(3)
                save_run_run_info[ln_idx] = (
                    path, _argv_for_save_run_run(ln_idx)
                )
                continue
            m_sr = WITH_SAVE_RUN_RE.match(stripped_line)
            if m_sr:
                # Save+run (Scratch) takes precedence over plain `with
                # "X":` and plain `with Scratch:` so the same line never
                # lands in two passes.
                path = m_sr.group(3)
                capture = m_sr.group(6)
                save_run_info[ln_idx] = (path, capture)
                continue
            m_ssr = WITH_SCRATCH_SAVE_RE.match(stripped_line)
            if m_ssr:
                # Reversed save+run shape: `with Scratch: "name.py"`.
                # Same dict as the forward shape so Pass 1.4 handles
                # both identically.
                capture = m_ssr.group(3)
                path = m_ssr.group(5)
                save_run_info[ln_idx] = (path, capture)
                continue
            if WITH_STR_RE.match(line):
                str_lines.add(ln_idx)
            if WITH_SCRATCH_RE.match(line):
                scratch_lines.add(ln_idx)
            if WITH_BASH_RE.match(line):
                bash_lines.add(ln_idx)
            if WITH_RUN_RE.match(line):
                run_lines.add(ln_idx)
        return (str_lines, scratch_lines, bash_lines, run_lines,
                save_run_info, save_run_run_info)

    skip_types = {
        tokenize.NL, tokenize.NEWLINE, tokenize.COMMENT,
        tokenize.ENCODING, tokenize.INDENT, tokenize.DEDENT,
        tokenize.ENDMARKER,
    }
    code = [t for t in toks if t.type not in skip_types]

    for i, t in enumerate(code):
        if not (t.type == tokenize.NAME and t.string == "with"):
            continue
        if i + 2 >= len(code):
            continue
        a = code[i + 1]
        b = code[i + 2]

        # Save+run forms: `with "X" as Scratch:`, `with "X" as Scratch as h:`,
        # `with "X", Scratch:`, `with "X", Scratch as h:`. Checked BEFORE
        # the plain `with "X":` form so the same line never lands in both
        # `str_lines` and `save_run_info`.
        if a.type == tokenize.STRING and i + 4 < len(code):
            sep = code[i + 2]
            scratch_tok = code[i + 3]
            after_scratch = code[i + 4]
            is_as_form = (sep.type == tokenize.NAME and sep.string == "as")
            is_comma_form = (sep.type == tokenize.OP and sep.string == ",")
            scratch_match = (
                (is_as_form or is_comma_form)
                and scratch_tok.type == tokenize.NAME
                and scratch_tok.string in ("Scratch", "_", "__")
            )
            if scratch_match:
                try:
                    path_str = ast.literal_eval(a.string)
                except Exception:
                    path_str = None
                if isinstance(path_str, str):
                    # Bare colon: no capture variable.
                    if (after_scratch.type == tokenize.OP
                            and after_scratch.string == ":"):
                        save_run_info[t.start[0]] = (path_str, None)
                        continue
                    # `as <name>:` capture form.
                    if (after_scratch.type == tokenize.NAME
                            and after_scratch.string == "as"
                            and i + 6 < len(code)
                            and code[i + 5].type == tokenize.NAME
                            and code[i + 6].type == tokenize.OP
                            and code[i + 6].string == ":"):
                        save_run_info[t.start[0]] = (
                            path_str, code[i + 5].string
                        )
                        continue

        # Save+RUN forms: `with "X" as RUN:` and `with "X", RUN:`.
        # Checked BEFORE the plain `with "X":` form so the same line
        # never lands in both `str_lines` and `save_run_run_info`. The
        # `as RUN` token sequence cannot collide with the save+Scratch
        # block above (different name token), so order between the two
        # save+run checks doesn't matter — they're mutually exclusive.
        # Inline argv (e.g. `with "X" as RUN: -O`) was sanitized away
        # before tokenize, so we only see the bare-colon form here and
        # re-derive argv from the original source line.
        if a.type == tokenize.STRING and i + 4 < len(code):
            sep = code[i + 2]
            run_tok = code[i + 3]
            after_run = code[i + 4]
            is_as_form = (sep.type == tokenize.NAME and sep.string == "as")
            is_comma_form = (sep.type == tokenize.OP and sep.string == ",")
            run_match = (
                (is_as_form or is_comma_form)
                and run_tok.type == tokenize.NAME
                and run_tok.string == "RUN"
                and after_run.type == tokenize.OP
                and after_run.string == ":"
            )
            if run_match:
                try:
                    path_str = ast.literal_eval(a.string)
                except Exception:
                    path_str = None
                if isinstance(path_str, str):
                    save_run_run_info[t.start[0]] = (
                        path_str, _argv_for_save_run_run(t.start[0])
                    )
                    continue

        if a.type == tokenize.STRING and b.type == tokenize.OP and b.string == ":":
            str_lines.add(t.start[0])
            continue

        if a.type == tokenize.NAME and a.string == "bash":
            if b.type == tokenize.OP and b.string == ":":
                bash_lines.add(t.start[0])
                continue

        if a.type == tokenize.NAME and a.string == "RUN":
            if b.type == tokenize.OP and b.string == ":":
                run_lines.add(t.start[0])
                continue

        if a.type == tokenize.NAME and a.string in ("Scratch", "_", "__"):
            # Figure out whether this is `with Scratch:` (or `... as h:`)
            # and where the colon sits — then peek past the colon for an
            # immediate STRING token, which signals the reversed save+run
            # shape `with Scratch: "name.py"` (or `with Scratch as a:
            # "name.py"`). Same precedence rule as the forward save+run
            # shape: route to `save_run_info` so the same line never
            # also lands in `scratch_lines`.
            capture_name = None
            after_colon_idx = None
            if b.type == tokenize.OP and b.string == ":":
                after_colon_idx = i + 3
            elif (
                b.type == tokenize.NAME and b.string == "as"
                and i + 4 < len(code)
                and code[i + 3].type == tokenize.NAME
                and code[i + 4].type == tokenize.OP
                and code[i + 4].string == ":"
            ):
                capture_name = code[i + 3].string
                after_colon_idx = i + 5

            if after_colon_idx is not None:
                if (after_colon_idx < len(code)
                        and code[after_colon_idx].type == tokenize.STRING):
                    try:
                        path_str = ast.literal_eval(
                            code[after_colon_idx].string
                        )
                    except Exception:
                        path_str = None
                    if isinstance(path_str, str):
                        save_run_info[t.start[0]] = (path_str, capture_name)
                        continue
                scratch_lines.add(t.start[0])

    return (str_lines, scratch_lines, bash_lines, run_lines,
            save_run_info, save_run_run_info)


def _resolve_file_path(path_str: str, files_dir: Path, notebook_dir: Path) -> Path:
    """
    Resolve the target path for a `with "X":` block.

    Rule (kept simple on purpose so it matches what `open()` does at
    runtime, since the runner chdirs to `files_dir`):

      Absolute path (`/tmp/foo`, `C:\\...`)  -> exact path, untouched
      Anything else                          -> files_dir / path

    `notebook_dir` is accepted for backwards compatibility but no longer
    used; a `with "sub/foo.txt":` block now lives at
    `sandbox/files/sub/foo.txt`, so `open("sub/foo.txt")` from the
    notebook reads the same file.
    """
    p = Path(path_str)
    if p.is_absolute():
        return p
    return files_dir / p


def _dedent_body(body_lines, base_indent: int):
    """Remove up to `base_indent` chars of leading whitespace from each line."""
    out = []
    for line in body_lines:
        if line.strip() == "":
            out.append(line)
            continue
        head = line[:base_indent]
        if head.strip() == "":
            out.append(line[base_indent:])
        else:
            out.append(line)
    return out


def _gather_block_end(lines, start_idx: int, with_indent: int) -> int:
    """
    Return the index of the first line that ENDS the block (line whose indent
    is <= with_indent and which is non-blank), or len(lines) if EOF.
    Trailing blank lines INSIDE the block are still included up to the
    boundary; the caller can trim them as needed.
    """
    j = start_idx + 1
    while j < len(lines):
        line = lines[j]
        if line.strip() == "":
            j += 1
            continue
        line_indent = len(line) - len(line.lstrip())
        if line_indent <= with_indent:
            break
        j += 1
    return j


def _gather_raw_marker_end(lines, start_idx: int, marker: str):
    """Return the index of the closing raw-text marker line, if present."""
    j = start_idx + 1
    while j < len(lines):
        if lines[j].strip() == marker:
            return j
        j += 1
    return None


def _extract_str_block_body(lines, start_idx: int, with_indent: int,
                            allow_same_level_raw: bool):
    """Extract a `with "X":` body as dedented text or triple-quoted raw text."""
    if allow_same_level_raw:
        marker_idx = start_idx + 1
        while marker_idx < len(lines) and lines[marker_idx].strip() == "":
            marker_idx += 1

        if marker_idx < len(lines):
            marker = lines[marker_idx].strip()
            if marker in RAW_TEXT_MARKERS:
                closing_idx = _gather_raw_marker_end(lines, marker_idx, marker)
                if closing_idx is not None:
                    return lines[marker_idx + 1:closing_idx], closing_idx + 1

    block_end = _gather_block_end(lines, start_idx, with_indent)

    body_end = block_end
    while body_end > start_idx + 1 and lines[body_end - 1].strip() == "":
        body_end -= 1

    body_lines = lines[start_idx + 1:body_end]
    real_indent = _smallest_indent(body_lines, with_indent)
    return _dedent_body(body_lines, real_indent), block_end


def _preprocess_with_blocks(src: str, files_dir: Path, notebook_dir: Path,
                            *, allow_same_level_raw: bool = False):
    """
    Walk the source line by line.

        For every `with "filename":` block:
            - extract the body and dedent it, or if enabled by settings honor a
                triple-quoted same-level raw body, then write to disk
      - replace the `with` line + body lines with blank lines (line numbers
        in the rest of the file are preserved exactly)

    For every `with bash:` block:
      - record each non-blank, non-comment body line as a shell command
        keyed by its 1-based line number
      - blank out the entire block (header + body) so the runnable Python
        never sees these lines (line numbers preserved)

    For every `with RUN:` (or `with RUN: arg1 arg2 ...`) block:
      - extract and dedent the body, store keyed by the 1-based line number
        of the LAST non-blank body line (where annotations go)
      - blank out the entire block (header + body) so the runnable Python
        never sees these lines (line numbers preserved)

    For every `with Scratch:` / `with _:` / `with __:` block:
      - rewrite the `with` line so it calls a runtime context manager:
            `with __nb_Scratch__():`         (or `... as a:`)
        Body lines are left untouched (line numbers preserved).

    For every save-and-run block (`with "X" as Scratch:` and friends):
      - dedent the body and write it verbatim to the resolved path
        (same path rules as `with "X":`)
      - rewrite ONLY the `with` header to `with __nb_Scratch__():`
        (or `with __nb_Scratch__() as h:`) so the body runs in-process
        with normal Scratch isolation. Body lines are NOT blanked.
      - if the body is not valid Python, skip the file write and emit
        a `# !err: SyntaxError` annotation on the header line; the
        header is rewritten to `: pass` and the body is blanked so the
        rest of the notebook still parses and gets annotated.

    For every save-and-fresh-subprocess-run block (`with "X" as RUN:`
    / `with "X", RUN:`, with optional inline argv):
      - dedent the body and write it verbatim to the resolved path
        (same path rules as `with "X":`)
      - queue the body in `run_blocks` keyed by its LAST non-blank body
        line, so `_run_run_blocks` runs it in a fresh `python3` subprocess.
        Save+RUN entries carry the resolved saved-file path as the third
        tuple element (`saved_path`), so `_run_run_blocks` invokes
        python3 on the user-typed file directly and any traceback points
        at that path instead of a `.run_blocks/...` throwaway. Body
        annotations still land on the last body line.
      - blank out the entire block (header + body) so the runnable Python
        never sees these lines (full process isolation, like plain RUN)
      - if the body is not valid Python, DO NOT write the file, DO NOT
        queue the subprocess, and emit a `# !err: SyntaxError` annotation
        on the header line (mirrors `with "X" as Scratch:`). The body is
        already blanked so the rest of the notebook still parses.

    Returns (runnable_src, files_written, bash_commands, run_blocks,
    save_run_results).
    `bash_commands` is a dict: {body_line_number_1based: command_str}.
    `run_blocks` is a dict:
        {last_body_line_1based: (body_text, argv_list, saved_path_or_None)}.
    `saved_path` is the resolved `Path` written to disk for save+RUN
    blocks (`with "X" as RUN:` / `with "X", RUN:`), and `None` for plain
    `with RUN:` blocks. `_run_run_blocks` uses it to invoke python3 on
    the saved file directly when present, so tracebacks reference the
    user-typed path instead of a `.run_blocks/...` temp.
    `save_run_results` is a dict: {with_line_1based: [(prefix, text), ...]}
    used to splice annotations (currently only SyntaxError reports) onto
    save+run header lines after the run.
    """
    lines = src.splitlines(keepends=True)
    files_written = []
    bash_commands: dict = {}
    run_blocks: dict = {}
    save_run_results: dict = {}

    (str_lines, scratch_lines, bash_lines, run_lines,
     save_run_info, save_run_run_info) = _find_magic_with_lines(src)

    # ---- Pass 1: extract `with "X":` blocks ----
    # Replace the `with` line and its body with blank lines so the surviving
    # source has identical line numbering. Doing this BEFORE pass 2 means
    # pass 2's empty-body detection sees the post-blanking state, which
    # matters when a Scratch block's only body is a nested `with "X":`.
    pass1 = list(lines)
    i = 0
    while i < len(lines):
        line = lines[i]
        line_num = i + 1

        m = WITH_STR_RE.match(line.rstrip("\n")) if line_num in str_lines else None
        if not m:
            i += 1
            continue

        indent_str = m.group(1)
        with_indent = len(indent_str)
        path_str = m.group(3)

        dedented, block_end = _extract_str_block_body(
            lines, i, with_indent, allow_same_level_raw
        )

        target = _resolve_file_path(path_str, files_dir, notebook_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("".join(dedented))
        files_written.append(str(target))

        # If this is a `.py` file inside a subdirectory of files_dir,
        # auto-create empty `__init__.py` files all the way up to (but
        # not including) files_dir, so `from subdir import foo` works.
        # Don't overwrite any existing `__init__.py` files.
        if target.suffix == ".py":
            try:
                rel_parent = target.parent.resolve().relative_to(
                    files_dir.resolve()
                )
            except ValueError:
                rel_parent = None
            if rel_parent is not None and rel_parent != Path("."):
                cur = files_dir.resolve()
                for part in rel_parent.parts:
                    cur = cur / part
                    init_file = cur / "__init__.py"
                    if not init_file.exists():
                        init_file.write_text("")

        for k in range(i, block_end):
            end = "\n" if lines[k].endswith("\n") else ""
            pass1[k] = end
        i = block_end

    # ---- Pass 1.4: extract `with "X" as Scratch:` save+run blocks ----
    # Combined "save the body to disk AND run it sandboxed" form. Walks
    # the ORIGINAL `lines` (not pass1) so the file written to disk is the
    # verbatim source the user typed, and rewrites ONLY the header line
    # in pass1 (body lines stay in place so they execute in-process).
    # Headers turn into `with __nb_Scratch__():` (or `... as h:`), which
    # the shim's AST transform later converts into a real function-scope
    # block — same isolation guarantees as plain `with Scratch:`.
    #
    # If the body fails to parse as Python, we DO NOT write the file (the
    # file should reflect runnable source, not garbage), AND we attach a
    # `# !err: SyntaxError` annotation to the header line, AND we blank
    # the body so the file still parses and the rest of the notebook can
    # be annotated.
    i = 0
    while i < len(lines):
        line_num = i + 1
        info = save_run_info.get(line_num)
        if info is None:
            i += 1
            continue

        path_str, capture_var = info
        line = lines[i]
        leading = len(line) - len(line.lstrip(" \t"))
        indent_str = line[:leading]
        with_indent = leading

        # Body comes from ORIGINAL source — file on disk should match
        # what the user typed, not the post-string-extraction state.
        block_end = _gather_block_end(lines, i, with_indent)
        body_end = block_end
        while body_end > i + 1 and lines[body_end - 1].strip() == "":
            body_end -= 1

        body_lines_orig = lines[i + 1:body_end]
        if body_lines_orig:
            real_indent = _smallest_indent(body_lines_orig, with_indent)
            dedented = _dedent_body(body_lines_orig, real_indent)
        else:
            dedented = []
        body_text = "".join(dedented)

        # Validate the body as Python before writing the file.
        valid = True
        syntax_err_msg = None
        if body_text.strip():
            try:
                ast.parse(body_text)
            except SyntaxError as exc:
                valid = False
                detail = exc.msg or "invalid syntax"
                if exc.lineno:
                    syntax_err_msg = (
                        f"SyntaxError: {detail} (body line {exc.lineno})"
                    )
                else:
                    syntax_err_msg = f"SyntaxError: {detail}"

        if valid:
            target = _resolve_file_path(path_str, files_dir, notebook_dir)
            target.parent.mkdir(parents=True, exist_ok=True)
            # Clean-save: strip notebook annotations (`# in:` / `# out:` /
            # `# val:` / `# !err:` / `# err:`) before writing so the file
            # on disk is a runnable script, not a notebook copy. Iterated
            # saves stay flat instead of growing taller every run.
            target.write_text(_strip_for_clean_save(body_text))
            files_written.append(str(target))

            # Same `__init__.py` auto-creation as Pass 1, so a save+run
            # block at `with "pkg/util.py" as Scratch:` is importable as
            # `from pkg import util` later in the same notebook.
            if target.suffix == ".py":
                try:
                    rel_parent = target.parent.resolve().relative_to(
                        files_dir.resolve()
                    )
                except ValueError:
                    rel_parent = None
                if rel_parent is not None and rel_parent != Path("."):
                    cur = files_dir.resolve()
                    for part in rel_parent.parts:
                        cur = cur / part
                        init_file = cur / "__init__.py"
                        if not init_file.exists():
                            init_file.write_text("")
        else:
            save_run_results[line_num] = [("# !err:", syntax_err_msg)]

        as_part = f" as {capture_var}" if capture_var else ""
        if valid and body_lines_orig:
            new_header = f"{indent_str}with __nb_Scratch__(){as_part}:"
        else:
            # Empty OR invalid body — emit a one-liner so the file still
            # parses, and (if invalid) blank the body lines in pass1 so
            # they can't break the surrounding notebook.
            new_header = (
                f"{indent_str}with __nb_Scratch__(){as_part}: pass"
            )
            if not valid:
                for k in range(i + 1, body_end):
                    end = "\n" if pass1[k].endswith("\n") else ""
                    pass1[k] = end

        if line.endswith("\n"):
            new_header += "\n"
        pass1[i] = new_header
        i = body_end

    # ---- Pass 1.45: extract `with "X" as RUN:` save+RUN blocks ----
    # Combined "save the body to disk AND run it in a fresh python3
    # subprocess" form. Walks the ORIGINAL `lines` (not pass1) so the
    # file written to disk is the verbatim source the user typed. The
    # body is queued into `run_blocks` (the same dict that plain
    # `with RUN:` uses) so `_run_run_blocks` handles it identically:
    # fresh python3 process, body's `# in:` directives feed stdin, the
    # outer notebook's `# in:` queue is NOT shared, and stdout / stderr
    # / non-zero-exit annotations land under the LAST non-blank body
    # line. Header + body are then blanked in pass1 so the runnable
    # Python doesn't try to execute the body in the notebook process
    # (the whole point is process isolation, stronger than Scratch's).
    #
    # If the body fails to parse as Python, we DO NOT write the file
    # and DO NOT queue the subprocess (mirrors `with "X" as Scratch:`);
    # a `# !err: SyntaxError` annotation is attached to the header line
    # via `save_run_results`, and the body is blanked so the rest of
    # the notebook still parses.
    i = 0
    while i < len(lines):
        line_num = i + 1
        info = save_run_run_info.get(line_num)
        if info is None:
            i += 1
            continue

        path_str, argv = info
        line = lines[i]
        leading = len(line) - len(line.lstrip(" \t"))
        with_indent = leading

        # Body comes from ORIGINAL source — file on disk should match
        # what the user typed, not the post-string-extraction state.
        block_end = _gather_block_end(lines, i, with_indent)
        body_end = block_end
        while body_end > i + 1 and lines[body_end - 1].strip() == "":
            body_end -= 1

        body_lines_orig = lines[i + 1:body_end]
        if body_lines_orig:
            real_indent = _smallest_indent(body_lines_orig, with_indent)
            dedented = _dedent_body(body_lines_orig, real_indent)
        else:
            dedented = []
        body_text = "".join(dedented)

        # Validate the body as Python before writing the file.
        valid = True
        syntax_err_msg = None
        if body_text.strip():
            try:
                ast.parse(body_text)
            except SyntaxError as exc:
                valid = False
                detail = exc.msg or "invalid syntax"
                if exc.lineno:
                    syntax_err_msg = (
                        f"SyntaxError: {detail} (body line {exc.lineno})"
                    )
                else:
                    syntax_err_msg = f"SyntaxError: {detail}"

        if valid and body_text.strip():
            target = _resolve_file_path(path_str, files_dir, notebook_dir)
            target.parent.mkdir(parents=True, exist_ok=True)
            # Clean-save: same rationale as Pass 1.4 — the saved file
            # should be a runnable script, not a notebook with stale
            # `# in:` / `# out:` / `# val:` / `# !err:` / `# err:` lines.
            # NOTE: the subprocess still gets the ORIGINAL body_text via
            # `run_blocks` below, so its own `# in:` directives still
            # feed stdin (only the FILE on disk is cleaned).
            target.write_text(_strip_for_clean_save(body_text))
            files_written.append(str(target))

            # Same `__init__.py` auto-creation as Pass 1, so a save+RUN
            # block at `with "pkg/util.py" as RUN:` is importable as
            # `from pkg import util` from elsewhere later. (The body
            # itself runs in a fresh subprocess, so the helper is
            # primarily useful to OTHER blocks in the same notebook.)
            if target.suffix == ".py":
                try:
                    rel_parent = target.parent.resolve().relative_to(
                        files_dir.resolve()
                    )
                except ValueError:
                    rel_parent = None
                if rel_parent is not None and rel_parent != Path("."):
                    cur = files_dir.resolve()
                    for part in rel_parent.parts:
                        cur = cur / part
                        init_file = cur / "__init__.py"
                        if not init_file.exists():
                            init_file.write_text("")

            # Annotations land under the LAST non-blank body line —
            # `body_end` is the slice index just past the last body
            # line, which equals the 1-based line number of that last
            # body line.
            last_body_line = body_end
            # Pass the resolved saved-file path so `_run_run_blocks`
            # invokes python3 on THAT file directly — any traceback then
            # references the user-typed path (e.g. `sandbox/files/name.py`)
            # instead of the throwaway `.run_blocks/...` temp file.
            run_blocks[last_body_line] = (body_text, argv, target)
        elif not valid:
            save_run_results[line_num] = [("# !err:", syntax_err_msg)]

        # Blank out header + body so the runnable Python never sees
        # them. Empty-body case also lands here (no file write, no
        # queue, no annotation — just a blanked-out header).
        for k in range(i, body_end):
            end = "\n" if pass1[k].endswith("\n") else ""
            pass1[k] = end
        i = body_end

    # ---- Pass 1.5: extract `with bash:` blocks ----
    # Walk the pass1 source so any nested string-extraction blocks (already
    # blanked above) won't be mistaken for shell commands. Each non-blank,
    # non-comment body line becomes a shell command keyed by its 1-based
    # line number; the entire block (header + body) is then blanked so the
    # surviving runnable Python doesn't see these lines.
    i = 0
    while i < len(pass1):
        line = pass1[i]
        line_num = i + 1

        m = WITH_BASH_RE.match(line.rstrip("\n")) if line_num in bash_lines else None
        if not m:
            i += 1
            continue

        with_indent = len(m.group(1))
        block_end = _gather_block_end(pass1, i, with_indent)

        body_end = block_end
        while body_end > i + 1 and pass1[body_end - 1].strip() == "":
            body_end -= 1

        for k in range(i + 1, body_end):
            bl = pass1[k]
            stripped = bl.strip()
            if not stripped or stripped.startswith("#"):
                continue
            bash_commands[k + 1] = stripped

        for k in range(i, body_end):
            end = "\n" if pass1[k].endswith("\n") else ""
            pass1[k] = end
        i = body_end

    # ---- Pass 1.6: extract `with RUN:` blocks ----
    # Walk the post-string-extraction source so a nested `with "X":` block
    # whose contents happen to look like a RUN body cannot leak in. Each
    # block's body is dedented and stashed as a single string keyed by the
    # 1-based line number of its LAST non-blank body line — that's where
    # the # out: / # err: annotations get spliced after the subprocess
    # finishes. The whole block (header + body) is then blanked so the
    # runnable Python doesn't try to execute the body in the notebook
    # process (the whole point is fresh-process isolation).
    i = 0
    while i < len(pass1):
        line = pass1[i]
        line_num = i + 1

        m = WITH_RUN_RE.match(line.rstrip("\n")) if line_num in run_lines else None
        if not m:
            i += 1
            continue

        with_indent = len(m.group(1))
        args_str = m.group(2) or ""
        try:
            argv = shlex.split(args_str) if args_str else []
        except ValueError:
            # Malformed quoting — treat as no args rather than crashing
            # the whole notebook run.
            argv = []

        block_end = _gather_block_end(pass1, i, with_indent)

        body_end = block_end
        while body_end > i + 1 and pass1[body_end - 1].strip() == "":
            body_end -= 1

        body_lines = pass1[i + 1:body_end]
        if body_lines:
            real_indent = _smallest_indent(body_lines, with_indent)
            dedented = _dedent_body(body_lines, real_indent)
            body_text = "".join(dedented)
            # 1-based line number of the last non-blank body line.
            last_body_line = body_end
            # Plain `with RUN:` has no user-saved file; `_run_run_blocks`
            # will write a throwaway temp file under `.run_blocks/`.
            run_blocks[last_body_line] = (body_text, argv, None)

        for k in range(i, body_end):
            end = "\n" if pass1[k].endswith("\n") else ""
            pass1[k] = end
        i = body_end

    # ---- Pass 2: rewrite `with Scratch:` blocks ----
    # Operate on the pass1 source so empty-body detection accounts for
    # already-blanked nested string-extraction blocks.
    out = list(pass1)
    i = 0
    while i < len(pass1):
        line = pass1[i]
        line_num = i + 1

        m = WITH_SCRATCH_RE.match(line.rstrip("\n")) if line_num in scratch_lines else None
        if not m:
            i += 1
            continue

        indent = m.group(1)
        as_part = m.group(3) or ""
        with_indent = len(indent)

        # Detect an empty body (no non-blank line indented deeper than
        # the with-line) on the pass1 source. Without this, a Scratch
        # block whose only body is a string-extraction block (now blanked
        # in pass1) would rewrite to `with __nb_Scratch__():` and Python
        # would refuse to parse the whole file with an IndentationError,
        # killing all annotations on the rest of the notebook.
        scratch_block_end = _gather_block_end(pass1, i, with_indent)
        has_body = False
        for k in range(i + 1, scratch_block_end):
            bl = pass1[k]
            if bl.strip() == "":
                continue
            bl_indent = len(bl) - len(bl.lstrip())
            if bl_indent > with_indent:
                has_body = True
                break

        if has_body:
            new_line = f"{indent}with __nb_Scratch__(){as_part}:"
        else:
            # Effectively empty body — emit a one-line `... : pass` so
            # the file still parses and the rest of the notebook gets
            # annotated normally. The block does nothing (no captures,
            # no isolation work to do).
            new_line = f"{indent}with __nb_Scratch__(){as_part}: pass"

        if line.endswith("\n"):
            new_line += "\n"
        out[i] = new_line
        i += 1

    return ("".join(out), files_written, bash_commands, run_blocks,
            save_run_results)


def _smallest_indent(body_lines, with_indent: int) -> int:
    """Find the smallest indentation (in spaces) on any non-blank body line."""
    smallest = None
    for line in body_lines:
        if line.strip() == "":
            continue
        ind = len(line) - len(line.lstrip())
        if ind <= with_indent:
            # Shouldn't happen for a valid block, but be defensive.
            continue
        if smallest is None or ind < smallest:
            smallest = ind
    return smallest if smallest is not None else with_indent + 4


# ---------- AST helpers ----------

def _is_print_call(node):
    if not isinstance(node, ast.Call):
        return False
    func = node.func
    return isinstance(func, ast.Name) and func.id == "print"


def _is_docstring(node):
    return isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)


def _find_bare_expr_lines(src: str) -> set:
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return set()
    bare = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr):
            if _is_print_call(node.value):
                continue
            if _is_docstring(node):
                continue
            bare.add(node.lineno)
    return bare


# ---------- input directive parsing ----------

def _parse_all_inputs(src: str):
    """
    Walk the source in order. Collect:
      - `# in: <value>`        -> one value
      - `# setin(...)`         -> tuple/list payload
      - `# setin a, b, c`      -> CSV payload
      - `# setin` then `# x`   -> block-style payload
    Returns the combined list in source order.
    """
    inputs = []
    lines = src.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        m = re.match(r"^\s*#\s*in:\s*(.*)$", line)
        if m:
            inputs.append(m.group(1))
            i += 1
            continue

        m = re.match(r"^\s*#\s*setin\b(.*)$", line)
        if m:
            tail = m.group(1).strip()
            if tail:
                if tail.startswith("(") or tail.startswith("["):
                    try:
                        value = ast.literal_eval(tail)
                        if isinstance(value, (list, tuple)):
                            inputs.extend(str(v) for v in value)
                        else:
                            inputs.append(str(value))
                    except Exception:
                        parts = [p.strip().strip("\"'") for p in tail.split(",")]
                        inputs.extend(p for p in parts if p)
                else:
                    parts = [p.strip().strip("\"'") for p in tail.split(",")]
                    inputs.extend(p for p in parts if p)
                i += 1
                continue

            # Block form
            j = i + 1
            while j < len(lines):
                comment = re.match(r"^\s*#(.*)$", lines[j])
                if not comment:
                    break
                body = comment.group(1).strip()
                if not body:
                    break
                if re.match(r"^(zy:|fig:|quick:|note:|save:|setin\b|in:)", body):
                    break
                inputs.append(body)
                j += 1
            i = j
            continue

        i += 1

    return inputs


# ---------- shim builder ----------

skip_none_flag = False


def _build_shim(read_path: Path, file_attr_path: Path,
                bare_lines: set, inputs: list,
                files_dir: Path,
                notebook_dir: Path) -> str:
    """
    `read_path`        — file the shim opens to read source (the temp runnable)
    `file_attr_path`   — what the user's code sees as `__file__` and what
                         appears in tracebacks (the original goog.py)
    `files_dir`        — sandbox/files/, prepended to sys.path so user-written
                         `with "helper.py":` files are importable as
                         `import helper` from the notebook in the same run.
                         Each notebook run is a fresh subprocess, so cached
                         modules from a previous run are gone automatically.
    `notebook_dir`     — sandbox/notebook/, also prepended to sys.path so any
                         sibling package next to goog.py (e.g. `Helpers/`,
                         `Stuff/`, etc.) is importable. Matches Python's
                         "module next to script" intuition.
    """
    bare_lines_repr = repr(sorted(bare_lines))
    files_dir_repr = repr(str(files_dir.resolve()))
    notebook_dir_repr = repr(str(notebook_dir.resolve()))
    return (
        "import sys, builtins, inspect, ast, io\n"
        # Prepend sandbox/notebook/ first, then sandbox/files/. Net order
        # at runtime is [files_dir, notebook_dir, ...], so a freshly-written
        # `with "Helpers.py":` body wins over the sibling `Helpers/` package
        # (last action wins, by design).
        f"sys.path.insert(0, {notebook_dir_repr})\n"
        f"sys.path.insert(0, {files_dir_repr})\n"
        "_orig_print = builtins.print\n"
        "_orig_input = builtins.input\n"
        # Stack of active `with Scratch as a:` capture frames. Each frame
        # is a dict {'out': [str], 'err': [str]}. `_tagged_print` and the
        # tee'd `sys.stderr.write` push to the topmost frame so the
        # `as a:` binding gets `a.out` / `a.err` / `a.outs` populated
        # with whatever the body printed. The stack is push/pop'd by
        # `__nb_capture__` (below) — empty stack means no capture, no-op.
        "_capture_stack = []\n"
        "def _tagged_print(*args, **kwargs):\n"
        "    frame = inspect.currentframe().f_back\n"
        "    lineno = frame.f_lineno\n"
        "    buf = io.StringIO()\n"
        "    kwargs2 = dict(kwargs); kwargs2['file'] = buf; kwargs2.pop('flush', None)\n"
        "    _orig_print(*args, **kwargs2)\n"
        "    text = buf.getvalue().rstrip('\\n')\n"
        "    pieces = text.split('\\n')\n"
        "    for piece in pieces:\n"
        "        sys.stdout.write(f'__OUT__{lineno}__{piece}\\n')\n"
        "    sys.stdout.flush()\n"
        "    if _capture_stack:\n"
        "        _capture_stack[-1]['out'].extend(pieces)\n"
        "builtins.print = _tagged_print\n"
        "\n"
        f"_INPUTS = {repr(inputs)}\n"
        "_input_iter = iter(_INPUTS)\n"
        "def _piped_input(prompt=''):\n"
        "    frame = inspect.currentframe().f_back\n"
        "    lineno = frame.f_lineno\n"
        "    try:\n"
        "        value = str(next(_input_iter))\n"
        "    except StopIteration:\n"
        "        return _orig_input(prompt)\n"
        "    sys.stdout.write(f'__OUT__{lineno}__{prompt}{value}\\n')\n"
        "    sys.stdout.flush()\n"
        "    return value\n"
        "builtins.input = _piped_input\n"
        "builtins._original_input_backup = _orig_input\n"
        "\n"
        "def _show_val(value, lineno):\n"
        f"    if {repr(skip_none_flag)} and value is None:\n"
        "        return\n"
        "    if isinstance(value, str):\n"
        "        pieces = value.splitlines() or ['']\n"
        "    else:\n"
        "        pieces = repr(value).split('\\n')\n"
        "    for piece in pieces:\n"
        "        sys.stdout.write(f'__VAL__{lineno}__{piece}\\n')\n"
        "    sys.stdout.flush()\n"
        "\n"
        # Namespace object that wraps a dict (the function's locals()).
        "class __NB_NS__:\n"
        "    def __init__(self, d=None):\n"
        "        if d:\n"
        "            for k, v in d.items():\n"
        "                if not k.startswith('__'):\n"
        "                    object.__setattr__(self, k, v)\n"
        "    def __repr__(self):\n"
        "        items = ', '.join(f'{k}={v!r}' for k, v in vars(self).items())\n"
        "        return f'Scratch({items})'\n"
        "\n"
        # Fallback runtime class: only invoked if the AST transform somehow
        # misses a `with __nb_Scratch__():` call. Same shape as a real CM so
        # nothing crashes; behaves like an identity passthrough.
        "class __nb_Scratch__:\n"
        "    def __enter__(self): return __NB_NS__()\n"
        "    def __exit__(self, *exc): return False\n"
        "\n"
        # Capture wrapper for `with Scratch as a:` (and reversed/save+run
        # variants). The AST transform routes the `as a:` form through
        # this so `a.out` / `a.err` / `a.outs` get populated with whatever
        # the body printed (or wrote to sys.stderr). Without `as` we skip
        # the wrapper entirely — no need to capture if nobody can see it.
        #
        # `out`  -> list[str], one entry per printed LINE (newline-split,
        #           same pieces _tagged_print writes to stdout markers).
        # `err`  -> list[str], one entry per stderr LINE (raw write tee).
        # `outs` -> the joined `\\n`.join(out) string for `print(a.outs)`
        #           one-liners — the most common 'type the output' shape.
        #
        # Stderr capture works by swapping sys.stderr for a tee object
        # only while the body runs; the original stream is restored in a
        # finally block. Print failures (or any exception) inside the
        # body propagate normally; we still pop the frame and restore
        # stderr so subsequent blocks aren't affected.
        "class _NB_StderrTee:\n"
        "    def __init__(self, inner): self._inner = inner; self._buf = ''\n"
        "    def write(self, s):\n"
        "        n = self._inner.write(s)\n"
        "        if _capture_stack:\n"
        "            self._buf += s\n"
        "            while '\\n' in self._buf:\n"
        "                line, self._buf = self._buf.split('\\n', 1)\n"
        "                _capture_stack[-1]['err'].append(line)\n"
        "        return n\n"
        "    def flush(self):\n"
        "        return self._inner.flush()\n"
        "    def __getattr__(self, name):\n"
        "        return getattr(self._inner, name)\n"
        "\n"
        "def __nb_capture__(ns_cls, fn):\n"
        "    cap = {'out': [], 'err': []}\n"
        "    _capture_stack.append(cap)\n"
        "    _orig_stderr = sys.stderr\n"
        "    sys.stderr = _NB_StderrTee(_orig_stderr)\n"
        "    try:\n"
        "        result = fn()\n"
        "    finally:\n"
        "        # Flush any trailing partial-line stderr text into err[].\n"
        "        tee = sys.stderr\n"
        "        if isinstance(tee, _NB_StderrTee) and tee._buf:\n"
        "            cap['err'].append(tee._buf)\n"
        "            tee._buf = ''\n"
        "        sys.stderr = _orig_stderr\n"
        "        _capture_stack.pop()\n"
        "    ns = ns_cls(result)\n"
        "    object.__setattr__(ns, 'out', cap['out'])\n"
        "    object.__setattr__(ns, 'err', cap['err'])\n"
        "    object.__setattr__(ns, 'outs', '\\n'.join(cap['out']))\n"
        "    return ns\n"
        "\n"
        f"_BARE_LINES = set({bare_lines_repr})\n"
        "\n"
        f"_src = open(r'{read_path}').read()\n"
        "_tree = ast.parse(_src, filename=r'{path}')\n".replace("{path}", str(file_attr_path)) +
        "\n"
        "import builtins as _bi\n"
        "_bi._show_val = _show_val\n"
        "\n"
        # Pass 1: turn `with __nb_Scratch__():` (with optional `as` capture)
        # into a real nested function definition + call. This gives true
        # scope isolation at any nesting level (module, function, class)
        # because Python's function scope already isolates locals.
        "class _ScratchTransform(ast.NodeTransformer):\n"
        "    def __init__(self):\n"
        "        self.counter = 0\n"
        "    def _is_scratch(self, ctx_expr):\n"
        "        return (isinstance(ctx_expr, ast.Call)\n"
        "                and isinstance(ctx_expr.func, ast.Name)\n"
        "                and ctx_expr.func.id == '__nb_Scratch__')\n"
        "    def visit_With(self, node):\n"
        "        node = self.generic_visit(node)\n"
        "        if len(node.items) != 1:\n"
        "            return node\n"
        "        item = node.items[0]\n"
        "        if not self._is_scratch(item.context_expr):\n"
        "            return node\n"
        "        self.counter += 1\n"
        "        fname = f'__sc_{self.counter}__'\n"
        "        return_locals = ast.Return(value=ast.Call(\n"
        "            func=ast.Name(id='locals', ctx=ast.Load()),\n"
        "            args=[], keywords=[]))\n"
        "        ast.copy_location(return_locals, node)\n"
        "        func = ast.FunctionDef(\n"
        "            name=fname,\n"
        "            args=ast.arguments(posonlyargs=[], args=[], vararg=None,\n"
        "                               kwonlyargs=[], kw_defaults=[],\n"
        "                               kwarg=None, defaults=[]),\n"
        "            body=node.body + [return_locals],\n"
        "            decorator_list=[], returns=None)\n"
        "        ast.copy_location(func, node)\n"
        "        call = ast.Call(func=ast.Name(id=fname, ctx=ast.Load()),\n"
        "                        args=[], keywords=[])\n"
        "        if item.optional_vars is not None:\n"
        # Capture form: route the function call through __nb_capture__
        # so the body's stdout / stderr land on `a.out` / `a.err` /
        # `a.outs` in addition to the namespace from `locals()`.
        "            wrapped = ast.Call(\n"
        "                func=ast.Name(id='__nb_capture__', ctx=ast.Load()),\n"
        "                args=[ast.Name(id='__NB_NS__', ctx=ast.Load()),\n"
        "                      ast.Name(id=fname, ctx=ast.Load())],\n"
        "                keywords=[])\n"
        "            target = item.optional_vars\n"
        "            target.ctx = ast.Store()\n"
        "            assign = ast.Assign(targets=[target], value=wrapped)\n"
        "            ast.copy_location(assign, node)\n"
        "            return [func, assign]\n"
        "        else:\n"
        # No-capture form: nothing reads stdout/stderr afterwards, so
        # skip the capture wrapper entirely (small perf win, also keeps
        # behavior unchanged for users who never opted into capture).
        "            wrapped = ast.Call(\n"
        "                func=ast.Name(id='__NB_NS__', ctx=ast.Load()),\n"
        "                args=[call], keywords=[])\n"
        "            expr = ast.Expr(value=wrapped)\n"
        "            ast.copy_location(expr, node)\n"
        "            return [func, expr]\n"
        "\n"
        # Pass 2: rewrite bare expressions to _show_val(expr, line). Same as v4.
        "class _Rewriter(ast.NodeTransformer):\n"
        "    def visit_Expr(self, node):\n"
        "        if node.lineno not in _BARE_LINES:\n"
        "            return node\n"
        "        new_call = ast.Call(\n"
        "            func=ast.Name(id='_show_val', ctx=ast.Load()),\n"
        "            args=[node.value, ast.Constant(value=node.lineno)],\n"
        "            keywords=[]\n"
        "        )\n"
        "        new_expr = ast.Expr(value=new_call)\n"
        "        return ast.copy_location(new_expr, node)\n"
        "\n"
        "_tree = _ScratchTransform().visit(_tree)\n"
        "_tree = _Rewriter().visit(_tree)\n"
        "ast.fix_missing_locations(_tree)\n"
        f"_code = compile(_tree, r'{file_attr_path}', 'exec')\n"
        "_globals = {'__name__': '__main__', '__file__': r'" + str(file_attr_path) + "',\n"
        "            '__nb_Scratch__': __nb_Scratch__,\n"
        "            '__NB_NS__': __NB_NS__,\n"
        "            '__nb_capture__': __nb_capture__}\n"
        "exec(_code, _globals)\n"
    )


def _run_bash_commands(commands: dict, files_dir: Path) -> dict:
    """
    Run each shell command via `/bin/sh -c` from `files_dir`. Returns a
    dict {line_number: [(prefix, text), ...]} ready for the splice loop.

    Per-line annotations:
      - each stdout line   -> ("# out:", line)
      - each stderr line   -> ("# err:", line)        (lowercase, distinct)
      - non-zero exit code -> ("# !err:", "exit code N")
      - 30s timeout        -> ("# !err:", "command exceeded 30s timeout")

    Each command runs synchronously, captured separately. A failure on one
    command does NOT abort other commands.
    """
    results: dict = {}
    for line_num, cmd in commands.items():
        annotations = []
        try:
            proc = subprocess.run(
                ["/bin/sh", "-c", cmd],
                capture_output=True,
                text=True,
                cwd=str(files_dir),
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            annotations.append(("# !err:", "command exceeded 30s timeout"))
            results[line_num] = annotations
            continue
        except Exception as exc:
            annotations.append(("# !err:", f"failed to run: {exc}"))
            results[line_num] = annotations
            continue

        for sl in proc.stdout.splitlines():
            annotations.append(("# out:", sl))
        for sl in proc.stderr.splitlines():
            annotations.append(("# err:", sl))
        if proc.returncode != 0:
            annotations.append(("# !err:", f"exit code {proc.returncode}"))
        results[line_num] = annotations
    return results


def _run_run_blocks(blocks: dict, files_dir: Path,
                    notebook_dir: Path) -> dict:
    """
    Run each `with RUN:` block in a fresh `python3` subprocess.

    For plain `with RUN:` blocks, the body is written to a uniquely-named
    temp file under `<files_dir>/.run_blocks/`, then invoked as
    `python3 [argv...] <tempfile>` from `files_dir`.

    For save+RUN blocks (`with "name.py" as RUN:`), the user already has
    an identical-content saved file at `<files_dir>/name.py`; we invoke
    python3 on THAT file directly so any error traceback references the
    path the user typed (e.g. `sandbox/files/name.py`) — exactly the file
    they can open and fix — instead of a throwaway temp under
    `.run_blocks/`. The saved file is NEVER deleted (it belongs to the
    user).

    Returns a dict {line_number: [(prefix, text), ...]} ready for the
    splice loop. The `line_number` key is the 1-based line number of the
    last non-blank body line in the original notebook source — every
    annotation for the block lands under that line.

    Per-block annotations:
      - each stdout line   -> ("# out:", line)
      - each stderr line   -> ("# err:", line)
      - non-zero exit code -> ("# !err:", "subprocess exited with code N")
      - exec failure       -> ("# !err:", "failed to run: <exc>")

    Temp files (plain RUN only) are deleted on success and KEPT on
    failure so Casey can poke at them for debugging.
    """
    results: dict = {}
    if not blocks:
        return results

    run_dir = files_dir / ".run_blocks"

    for line_num, value in blocks.items():
        # `run_blocks` value tuple shape:
        #   (body_text, argv, saved_path_or_None)
        # `saved_path` is set only for save+RUN blocks.
        body_text, argv, saved_path = value
        annotations = []

        if saved_path is not None:
            # Save+RUN: invoke the user-typed file directly so tracebacks
            # reference its real path. No temp file written, no cleanup.
            script_path = Path(saved_path)
            is_temp = False
        else:
            # Plain `with RUN:`: write a throwaway temp file.
            run_dir.mkdir(parents=True, exist_ok=True)
            # Unique-per-block temp filename: line number for human readability,
            # short uuid suffix to dodge collisions across runs.
            script_path = run_dir / f"run_L{line_num}_{uuid.uuid4().hex[:8]}.py"
            is_temp = True
            try:
                script_path.write_text(body_text)
            except Exception as exc:
                annotations.append(("# !err:", f"failed to write temp file: {exc}"))
                results[line_num] = annotations
                continue

        # Per-block stdin queue: only `# in:` directives INSIDE the
        # RUN body feed the subprocess. The outer notebook's queue is
        # intentionally not shared (the body has been blanked from the
        # `runnable` source already, so `_parse_all_inputs(runnable)`
        # in the outer flow can't see these). Each `# in:` value
        # becomes one line on stdin, in source order.
        stdin_inputs = _parse_all_inputs(body_text)
        # Always pass a (possibly-empty) stdin payload so subprocess.run
        # uses a PIPE and closes it after writing. Otherwise (input=None)
        # the child inherits the parent's real stdin — and any extra
        # `input()` call beyond the queue (or any input at all when the
        # queue is empty) would block forever waiting on a tty that
        # nobody's typing into. Closing the pipe means those input()
        # calls see EOF and raise EOFError, which surfaces as a normal
        # `# err:` traceback annotation instead of a hang.
        stdin_payload = "".join(s + "\n" for s in stdin_inputs)

        # Make sandbox/files/ importable inside the subprocess so
        # `import main` (and other helpers Casey wrote with `with
        # "X.py":`) resolve. The script lives in `.run_blocks/`, so
        # python3 only auto-prepends THAT to sys.path; we add files_dir
        # via PYTHONPATH so the subprocess matches what the in-process
        # notebook sees.
        env = os.environ.copy()
        files_dir_str = str(files_dir.resolve())
        notebook_dir_str = str(notebook_dir.resolve())
        existing_pp = env.get("PYTHONPATH", "")
        pp_parts = [files_dir_str, notebook_dir_str]
        if existing_pp:
            pp_parts.append(existing_pp)
        env["PYTHONPATH"] = os.pathsep.join(pp_parts)

        keep_temp = False
        # Note: Python normalizes the script argument to an absolute path
        # in tracebacks regardless of whether we pass a relative or
        # absolute path. For save+RUN that's fine — the absolute path
        # still ENDS in the user-typed name (e.g. `.../files/name.py`),
        # which is the file Casey can open and fix. Plain RUN keeps
        # showing its `.run_blocks/...` temp path (also fine — that file
        # is preserved on failure for poking).
        try:
            proc = subprocess.run(
                ["python3", *argv, str(script_path)],
                capture_output=True,
                text=True,
                cwd=str(files_dir),
                input=stdin_payload,
                env=env,
            )
        except Exception as exc:
            annotations.append(("# !err:", f"failed to run: {exc}"))
            # Keep the temp file on launch failure too — Casey can
            # eyeball it to see what was about to run.
            results[line_num] = annotations
            continue

        for sl in proc.stdout.splitlines():
            annotations.append(("# out:", sl))
        for sl in proc.stderr.splitlines():
            annotations.append(("# err:", sl))
        if proc.returncode != 0:
            annotations.append(
                ("# !err:", f"subprocess exited with code {proc.returncode}")
            )
            keep_temp = True

        # Only delete the throwaway temp script — never the user's
        # saved file.
        if is_temp and not keep_temp:
            try:
                script_path.unlink()
            except FileNotFoundError:
                pass

        results[line_num] = annotations
    return results


def _friendly_indent_error(src: str, exc: IndentationError):
    """Turn a Python IndentationError into a 1–3 line plain-language
    explanation that points at the line AND the previous line, since
    the issue is almost always a mismatch between the two.
    Returns a list of strings ready to be emitted as `# !err:` lines.
    """
    raw = exc.msg or "indentation problem"
    line_no = exc.lineno
    if not line_no:
        return [f"IndentationError: {raw}"]

    src_lines = src.splitlines()
    bad_line = src_lines[line_no - 1] if 0 < line_no <= len(src_lines) else ""
    bad_indent = len(bad_line) - len(bad_line.lstrip(" \t"))

    prev_idx = line_no - 2
    while prev_idx >= 0 and not src_lines[prev_idx].strip():
        prev_idx -= 1
    prev_line = src_lines[prev_idx] if prev_idx >= 0 else None
    prev_indent = (
        len(prev_line) - len(prev_line.lstrip(" \t")) if prev_line else 0
    )
    prev_no = prev_idx + 1 if prev_idx >= 0 else None

    low = raw.lower()
    msgs = []
    if "expected an indented block" in low:
        msgs.append(f"IndentationError on line {line_no}: this line needs to be indented.")
        if prev_no is not None and prev_line.rstrip().endswith(":"):
            msgs.append(
                f"  line {prev_no} ends with `:`, so line {line_no} should be "
                f"indented further (try {prev_indent + 4} spaces)."
            )
    elif "unindent does not match" in low:
        msgs.append(
            f"IndentationError on line {line_no}: indented {bad_indent} "
            f"space(s), but no open block matches that level."
        )
        if prev_no is not None:
            msgs.append(
                f"  line {prev_no} was indented {prev_indent} space(s) — pick "
                f"a level that lines up with an outer block."
            )
    elif "unexpected indent" in low:
        msgs.append(
            f"IndentationError on line {line_no}: indented {bad_indent} "
            f"space(s), but the previous line wasn't expecting a new block."
        )
        if prev_no is not None:
            msgs.append(
                f"  line {prev_no} was indented {prev_indent} space(s) — "
                f"line {line_no} probably wants the same."
            )
    elif "tab" in low and "space" in low:
        msgs.append(
            f"IndentationError on line {line_no}: tabs and spaces are mixed "
            f"in this block."
        )
        msgs.append(
            "  pick one (the runner already converts leading tabs to 4 "
            "spaces, but a tab in the middle of indentation can still slip in)."
        )
    else:
        msgs.append(f"IndentationError on line {line_no}: {raw}")
        if prev_no is not None:
            msgs.append(
                f"  line {line_no} indent: {bad_indent}; line {prev_no} "
                f"indent: {prev_indent}."
            )
    return msgs


def _friendly_syntax_error(exc: SyntaxError):
    """Brief friendly message for a non-indentation SyntaxError."""
    raw = exc.msg or "invalid syntax"
    if exc.lineno:
        return [f"SyntaxError on line {exc.lineno}: {raw}"]
    return [f"SyntaxError: {raw}"]


def _run_shim(shim_src: str):
    proc = subprocess.run(
        [sys.executable, "-c", shim_src],
        capture_output=True,
        text=True,
        timeout=30,
    )
    out_map, val_map = {}, {}
    for line in proc.stdout.splitlines():
        m = re.match(r"__OUT__(\d+)__(.*)", line)
        if m:
            out_map.setdefault(int(m.group(1)), []).append(m.group(2))
            continue
        m = re.match(r"__VAL__(\d+)__(.*)", line)
        if m:
            val_map.setdefault(int(m.group(1)), []).append(m.group(2))
    err_lines = []
    if proc.returncode != 0 and proc.stderr.strip():
        err_lines = ["--- ERROR ---"] + proc.stderr.splitlines()
    return out_map, val_map, err_lines


# ---------- main ----------

def run_and_annotate(path: str, *, skip_none: bool = False,
                     files_dir: Path = None) -> str:
    global skip_none_flag
    skip_none_flag = bool(skip_none)

    src_path = Path(path).resolve()
    notebook_dir = src_path.parent
    if files_dir is None:
        # Default: <sandbox-root>/files, where sandbox-root is the parent of
        # the notebook directory.
        files_dir = notebook_dir.parent / "files"
    files_dir = Path(files_dir)
    files_dir.mkdir(parents=True, exist_ok=True)

    original = src_path.read_text()
    allow_same_level_raw = _read_bool_workspace_setting(
        src_path.parent, SAME_LEVEL_RAW_WITH_SETTING, default=False
    )
    # Quietly fix common phone-typing whitespace mistakes (leading tabs,
    # non-breaking spaces) BEFORE anything else looks at the source, so
    # the preprocessor, parser, and our own error reporters all see a
    # consistent indent style.
    cleaned = _normalize_whitespace(_strip_old_annotations(original))

    # PRE-PROCESS the magic `with` blocks
    (runnable, files_written, bash_commands, run_blocks,
     save_run_results) = _preprocess_with_blocks(
        cleaned, files_dir, notebook_dir,
        allow_same_level_raw=allow_same_level_raw
    )

    # Pre-flight parse the runnable source. If it has an
    # IndentationError or SyntaxError, surface a friendly explanation
    # instead of letting the shim subprocess die with a raw Python
    # traceback. Line numbers in `runnable` match `cleaned` (the
    # preprocessor only blanks lines, never shifts them) so the
    # reported line numbers are meaningful to the user.
    preflight_err_lines = None
    try:
        ast.parse(runnable)
    except IndentationError as exc:
        preflight_err_lines = ["--- ERROR ---"] + _friendly_indent_error(
            cleaned, exc
        )
    except SyntaxError as exc:
        preflight_err_lines = ["--- ERROR ---"] + _friendly_syntax_error(exc)

    # Inputs (combine `# in:` and `# setin` in source order)
    inputs = _parse_all_inputs(runnable)

    # Bare expressions: parse the RUNNABLE source (it's valid Python now).
    bare_lines = _find_bare_expr_lines(runnable)

    if preflight_err_lines is not None:
        # Skip the shim — running broken Python would just produce a
        # noisier version of the same error. The friendly message is
        # spliced in below via `err_lines`.
        out_map, val_map, err_lines = {}, {}, preflight_err_lines
    else:
        # Write runnable to a SIBLING temp file so the user's file is never
        # overwritten until we have annotations to splice in. Tracebacks still
        # show the original goog.py path because we pass file_attr_path.
        runnable_path = src_path.with_name(src_path.name + ".__v6run__")
        runnable_path.write_text(runnable)
        try:
            shim = _build_shim(runnable_path, src_path, bare_lines, inputs,
                               files_dir, notebook_dir)
            out_map, val_map, err_lines = _run_shim(shim)
        finally:
            try:
                runnable_path.unlink()
            except FileNotFoundError:
                pass

    # Run any `with bash:` shell commands AFTER the Python notebook so
    # files Casey writes inside Python are visible to the shell. Each
    # command is independent and runs from `files_dir` (matching where
    # `with "X":` writes and where the notebook itself chdirs to).
    bash_results = _run_bash_commands(bash_commands, files_dir)

    # Same idea for `with RUN:` blocks — each runs in its own fresh
    # python3 subprocess from `files_dir`, after the notebook proper, so
    # files Casey writes from Python are visible to the subprocess too.
    run_results = _run_run_blocks(run_blocks, files_dir, notebook_dir)

    # Splice annotations back into CLEANED (so user keeps their original
    # `with "..."`/`with Scratch:`/`with bash:`/`with RUN:` syntax).
    new_lines = []
    for idx, line in enumerate(cleaned.splitlines(), start=1):
        new_lines.append(line)
        m = re.match(r"\s*", line)
        indent = m.group(0) if m else ""
        if idx in out_map:
            for out in out_map[idx]:
                new_lines.append(f"{indent}{OUT_PREFIX} {out}")
        if idx in val_map:
            for val in val_map[idx]:
                new_lines.append(f"{indent}{VAL_PREFIX} {val}")
        if idx in bash_results:
            for prefix, text in bash_results[idx]:
                new_lines.append(f"{indent}{prefix} {text}")
        if idx in run_results:
            for prefix, text in run_results[idx]:
                new_lines.append(f"{indent}{prefix} {text}")
        if idx in save_run_results:
            for prefix, text in save_run_results[idx]:
                new_lines.append(f"{indent}{prefix} {text}")

    if err_lines:
        while new_lines and new_lines[-1].strip() == "":
            new_lines.pop()
        for el in err_lines:
            new_lines.append(f"{ERR_PREFIX} {el}")

    final = "\n".join(new_lines) + "\n"
    src_path.write_text(final)

    # Auto-save based on magic comment (unchanged from v4)
    saved_to = _auto_save(src_path)

    counts = []
    if out_map:
        counts.append(f"{sum(len(v) for v in out_map.values())} print outputs")
    if val_map:
        counts.append(f"{sum(len(v) for v in val_map.values())} expression values")
    if bash_commands:
        counts.append(f"{len(bash_commands)} bash command(s)")
    if run_blocks:
        counts.append(f"{len(run_blocks)} run block(s)")
    summary = ", ".join(counts) if counts else "no output"

    msg = f"✅ Annotated {src_path.name} → {summary}."
    if files_written:
        msg += f"\n📝 Wrote {len(files_written)} file(s):"
        for f in files_written:
            msg += f"\n   - {f}"
    if saved_to:
        msg += f"\n💾 Auto-saved to: {saved_to}"
    if err_lines:
        msg += "\n⚠️  Had an error — see # !err: at bottom of file."
    return msg


# ---------- CLI ----------

if __name__ == "__main__":
    args = sys.argv[1:]
    skip_none = False
    if "--skip-none" in args:
        skip_none = True
        args.remove("--skip-none")

    if not args:
        print("Usage: python inline_output_v6.py <your_file.py> [--skip-none]")
        sys.exit(1)

    print(run_and_annotate(args[0], skip_none=skip_none))
