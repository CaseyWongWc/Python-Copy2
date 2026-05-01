"""
inline_output_v6.py
Casey's sandbox notebook — v4 + magic `with` blocks + `# in:` inputs.

What's NEW in v6 (on top of v4):

1.  `with "filename.ext":`
        The indented block becomes the file's CONTENTS (raw text, dedented).
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

Everything else from v4 still applies:
  -  print()                       -> `# out:`
  -  bare expressions              -> `# val:`  (with v4 string-splitting fix)
  -  errors                        -> `# !err:`
  -  # zy: / # fig: / # quick: / # note: / # save: magic auto-save
"""

import ast
import io
import re
import shutil
import subprocess
import sys
import tokenize
from pathlib import Path

OUT_PREFIX = "# out:"
VAL_PREFIX = "# val:"
ERR_PREFIX = "# !err:"


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
        if (
            stripped.startswith(OUT_PREFIX)
            or stripped.startswith(VAL_PREFIX)
            or stripped.startswith(ERR_PREFIX)
        ):
            continue
        keep.append(line)
    return "".join(keep)


# ---------- v6 preprocessor: magic `with` blocks ----------

WITH_STR_RE = re.compile(r'^(\s*)with\s+(["\'])(.+?)\2\s*:\s*$')
WITH_SCRATCH_RE = re.compile(
    r'^(\s*)with\s+(Scratch|__|_)(\s+as\s+\w+)?\s*:\s*$'
)


def _find_magic_with_lines(src: str):
    """
    Tokenize the source and return two sets of line numbers (1-based) where
    REAL magic `with` statements appear:
      - str_lines:     `with "X":`         (file-extraction form)
      - scratch_lines: `with Scratch:` etc. (sandbox-scope form)

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

    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        for ln_idx, line in enumerate(src.splitlines(), start=1):
            if WITH_STR_RE.match(line):
                str_lines.add(ln_idx)
            if WITH_SCRATCH_RE.match(line):
                scratch_lines.add(ln_idx)
        return str_lines, scratch_lines

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

        if a.type == tokenize.STRING and b.type == tokenize.OP and b.string == ":":
            str_lines.add(t.start[0])
            continue

        if a.type == tokenize.NAME and a.string in ("Scratch", "_", "__"):
            if b.type == tokenize.OP and b.string == ":":
                scratch_lines.add(t.start[0])
            elif (
                b.type == tokenize.NAME and b.string == "as"
                and i + 4 < len(code)
                and code[i + 3].type == tokenize.NAME
                and code[i + 4].type == tokenize.OP
                and code[i + 4].string == ":"
            ):
                scratch_lines.add(t.start[0])

    return str_lines, scratch_lines


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


def _preprocess_with_blocks(src: str, files_dir: Path, notebook_dir: Path):
    """
    Walk the source line by line.

    For every `with "filename":` block:
      - extract the body, dedent, write to disk
      - replace the `with` line + body lines with blank lines (line numbers
        in the rest of the file are preserved exactly)

    For every `with Scratch:` / `with _:` / `with __:` block:
      - rewrite the `with` line so it calls a runtime context manager:
            `with __nb_Scratch__():`         (or `... as a:`)
        Body lines are left untouched (line numbers preserved).

    Returns (runnable_src, files_written).
    """
    lines = src.splitlines(keepends=True)
    files_written = []

    str_lines, scratch_lines = _find_magic_with_lines(src)

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

        block_end = _gather_block_end(lines, i, with_indent)

        # Trim trailing blank lines from the body
        body_end = block_end
        while body_end > i + 1 and lines[body_end - 1].strip() == "":
            body_end -= 1

        body_lines = lines[i + 1:body_end]
        # Use the smallest indent on any non-blank body line as the dedent
        # amount, so 2-space, 4-space, and tab indents all work.
        real_indent = _smallest_indent(body_lines, with_indent)
        dedented = _dedent_body(body_lines, real_indent)

        target = _resolve_file_path(path_str, files_dir, notebook_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("".join(dedented))
        files_written.append(str(target))

        for k in range(i, body_end):
            end = "\n" if lines[k].endswith("\n") else ""
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

    return "".join(out), files_written


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
                bare_lines: set, inputs: list) -> str:
    """
    `read_path`        — file the shim opens to read source (the temp runnable)
    `file_attr_path`   — what the user's code sees as `__file__` and what
                         appears in tracebacks (the original goog.py)
    """
    bare_lines_repr = repr(sorted(bare_lines))
    return (
        "import sys, builtins, inspect, ast, io\n"
        "_orig_print = builtins.print\n"
        "_orig_input = builtins.input\n"
        "def _tagged_print(*args, **kwargs):\n"
        "    frame = inspect.currentframe().f_back\n"
        "    lineno = frame.f_lineno\n"
        "    buf = io.StringIO()\n"
        "    kwargs2 = dict(kwargs); kwargs2['file'] = buf; kwargs2.pop('flush', None)\n"
        "    _orig_print(*args, **kwargs2)\n"
        "    text = buf.getvalue().rstrip('\\n')\n"
        "    for piece in text.split('\\n'):\n"
        "        sys.stdout.write(f'__OUT__{lineno}__{piece}\\n')\n"
        "    sys.stdout.flush()\n"
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
        "            wrapped = ast.Call(\n"
        "                func=ast.Name(id='__NB_NS__', ctx=ast.Load()),\n"
        "                args=[call], keywords=[])\n"
        "            target = item.optional_vars\n"
        "            target.ctx = ast.Store()\n"
        "            assign = ast.Assign(targets=[target], value=wrapped)\n"
        "            ast.copy_location(assign, node)\n"
        "            return [func, assign]\n"
        "        else:\n"
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
        "            '__NB_NS__': __NB_NS__}\n"
        "exec(_code, _globals)\n"
    )


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
    cleaned = _strip_old_annotations(original)

    # PRE-PROCESS the magic `with` blocks
    runnable, files_written = _preprocess_with_blocks(
        cleaned, files_dir, notebook_dir
    )

    # Inputs (combine `# in:` and `# setin` in source order)
    inputs = _parse_all_inputs(runnable)

    # Bare expressions: parse the RUNNABLE source (it's valid Python now).
    bare_lines = _find_bare_expr_lines(runnable)

    # Write runnable to a SIBLING temp file so the user's file is never
    # overwritten until we have annotations to splice in. Tracebacks still
    # show the original goog.py path because we pass file_attr_path.
    runnable_path = src_path.with_name(src_path.name + ".__v6run__")
    runnable_path.write_text(runnable)
    try:
        shim = _build_shim(runnable_path, src_path, bare_lines, inputs)
        out_map, val_map, err_lines = _run_shim(shim)
    finally:
        try:
            runnable_path.unlink()
        except FileNotFoundError:
            pass

    # Splice annotations back into CLEANED (so user keeps their original
    # `with "..."`/`with Scratch:` syntax).
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
