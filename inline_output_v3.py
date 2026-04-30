"""
inline_output_v2.py
Casey's phone-shell-fix v2 — now Jupyter-style!

What's new in v2:
- Bare expressions on a line (like `1+1` or `name` or `obj.method()`) now also
  get their value inlined, labeled with `# val:` instead of `# out:`.
- This mimics what `InteractiveShell.ast_node_interactivity = "all"` does in
  IPython / Jupyter: every expression-statement shows its value, not just the
  last one.
- print() output still uses `# out:` (unchanged).
- Errors still use `# !err:` at bottom.

Usage (in Replit, on a fresh file):
    python inline_output_v2.py your_file.py

What you get:

    BEFORE                    AFTER
    -----                     -----
    print(1)                  print(1)
    1 + 1                     # out: 1
    x = 5                     1 + 1
    x                         # val: 2
    x * 2                     x = 5
                              x
                              # val: 5
                              x * 2
                              # val: 10

Rules for what counts as a "bare expression":
- Must be an Expression statement at the TOP level of a module, function,
  class, if/for/while/try/with body. (i.e., a line whose only purpose is
  evaluating a value)
- Calls to print() are ignored (handled by the print-shim).
- Calls whose return value is None (like `f.write(...)` or `f.close()`) will
  show `# val: None`. Use the --skip-none flag to hide those.
- String literals on their own (docstrings) are ignored.
- Assignments (`x = 5`) are NOT expressions — they don't print anything (same
  as Jupyter).
- Augmented assignments (`x += 1`) — same, no print.

Notes:
- Re-running on an annotated file: strips old `# out:` / `# val:` / `# !err:`
  lines first.
- All annotation lines preserve indentation.
- Multi-line outputs/values: each output line becomes its own comment.
"""

import ast
import re
import subprocess
import sys
from pathlib import Path

OUT_PREFIX = "# out:"   # from print()
VAL_PREFIX = "# val:"   # from bare expressions (Jupyter-style)
ERR_PREFIX = "# !err:"  # tracebacks


# ---------- helpers ----------

def _strip_old_annotations(src: str) -> str:
    """Remove lines that start with our annotation prefixes (after whitespace)."""
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


def _is_print_call(node: ast.expr) -> bool:
    """True if this expression is a call to the builtin print()."""
    if not isinstance(node, ast.Call):
        return False
    func = node.func
    if isinstance(func, ast.Name) and func.id == "print":
        return True
    return False


def _is_docstring(node: ast.Expr) -> bool:
    """True if this Expr statement is just a string literal (docstring/comment)."""
    return isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)


def _find_bare_expr_lines(src: str, skip_none: bool) -> set:
    """
    Walk the AST and return a set of line numbers where a bare expression
    statement lives (not a print, not a docstring).
    These are the lines we'll rewrite to ALSO emit a __VAL__ tag.
    """
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return set()

    bare_lines = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr):
            if _is_print_call(node.value):
                continue
            if _is_docstring(node):
                continue
            bare_lines.add(node.lineno)
    return bare_lines


# ---------- the main run ----------

def _build_shim(src_path: Path, bare_lines: set) -> str:
    """
    Build a Python shim that:
    1. Monkey-patches print() to tag each output with its source line.
    2. Reads the source, and for each bare-expression line, wraps it so that
       the resulting value is also tagged-printed.
    """
    bare_lines_repr = repr(sorted(bare_lines))
    return (
        "import sys, builtins, inspect, ast, io\n"
        "_orig_print = builtins.print\n"
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
        "def _show_val(value, lineno):\n"
        "    # Skip None if user asked\n"
        f"    if {repr(skip_none_flag)} and value is None:\n"
        "        return\n"
        "    if isinstance(value, str):\n"
        "        pieces = value.splitlines() or ['']\n"
        "        for piece in pieces:\n"
        "            sys.stdout.write(f'__OUT__{lineno}__{piece}\\n')\n"
        "    else:\n"
        "        text = repr(value)\n"
        "        for piece in text.split('\\n'):\n"
        "            sys.stdout.write(f'__VAL__{lineno}__{piece}\\n')\n"
        "    sys.stdout.flush()\n"
        "\n"
        f"_BARE_LINES = set({bare_lines_repr})\n"
        "\n"
        f"_src = open(r'{src_path}').read()\n"
        "_tree = ast.parse(_src, filename=r'{path}')\n".replace("{path}", str(src_path)) +
        "\n"
        "# Walk module + nested bodies, replace bare Expr nodes with a call to _show_val\n"
        "import builtins as _bi\n"
        "_bi._show_val = _show_val\n"
        "\n"
        "class _Rewriter(ast.NodeTransformer):\n"
        "    def visit_Expr(self, node):\n"
        "        if node.lineno not in _BARE_LINES:\n"
        "            return node\n"
        "        # Replace `expr` with `_show_val(expr, lineno)`\n"
        "        new_call = ast.Call(\n"
        "            func=ast.Name(id='_show_val', ctx=ast.Load()),\n"
        "            args=[node.value, ast.Constant(value=node.lineno)],\n"
        "            keywords=[]\n"
        "        )\n"
        "        new_expr = ast.Expr(value=new_call)\n"
        "        return ast.copy_location(new_expr, node)\n"
        "\n"
        "_tree = _Rewriter().visit(_tree)\n"
        "ast.fix_missing_locations(_tree)\n"
        f"_code = compile(_tree, r'{src_path}', 'exec')\n"
        "exec(_code, {'__name__': '__main__', '__file__': r'" + str(src_path) + "'})\n"
    )


# We use a module-level mutable to feed skip_none into the shim string above.
# (Cleaner than threading it through nested f-strings.)
skip_none_flag = False


def _run_shim(src_path: Path, shim_src: str) -> tuple:
    """Run the shim, parse output into (out_map, val_map, err_lines)."""
    proc = subprocess.run(
        [sys.executable, "-c", shim_src],
        capture_output=True,
        text=True,
        timeout=30,
    )
    out_map: dict[int, list[str]] = {}
    val_map: dict[int, list[str]] = {}
    for line in proc.stdout.splitlines():
        m = re.match(r"__OUT__(\d+)__(.*)", line)
        if m:
            ln = int(m.group(1))
            out_map.setdefault(ln, []).append(m.group(2))
            continue
        m = re.match(r"__VAL__(\d+)__(.*)", line)
        if m:
            ln = int(m.group(1))
            val_map.setdefault(ln, []).append(m.group(2))
            continue

    err_lines = []
    if proc.returncode != 0 and proc.stderr.strip():
        err_lines = ["--- ERROR ---"] + proc.stderr.splitlines()
    return out_map, val_map, err_lines


def run_and_annotate(path: str, skip_none: bool = False) -> str:
    global skip_none_flag
    skip_none_flag = bool(skip_none)

    src_path = Path(path)
    original = src_path.read_text()
    cleaned = _strip_old_annotations(original)
    src_path.write_text(cleaned)

    bare_lines = _find_bare_expr_lines(cleaned, skip_none=skip_none)
    shim = _build_shim(src_path, bare_lines)
    out_map, val_map, err_lines = _run_shim(src_path, shim)

    if not out_map and not val_map and not err_lines:
        src_path.write_text(original)
        return "No output captured. (File ran clean with no prints/expressions, or fatal error before any output.)"

    # Splice annotations after their source lines.
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
        new_lines.append("")
        for el in err_lines:
            new_lines.append(f"{ERR_PREFIX} {el}")

    final = "\n".join(new_lines) + "\n"
    src_path.write_text(final)

    counts = []
    if out_map:
        counts.append(f"{sum(len(v) for v in out_map.values())} print outputs")
    if val_map:
        counts.append(f"{sum(len(v) for v in val_map.values())} expression values")
    summary = ", ".join(counts) if counts else "no output"
    return f"✅ Annotated {src_path.name} → {summary}. Open the file to see them inlined."


# ---------- CLI ----------

if __name__ == "__main__":
    args = sys.argv[1:]
    skip_none = False
    if "--skip-none" in args:
        skip_none = True
        args.remove("--skip-none")

    if not args:
        print("Usage: python inline_output_v2.py <your_file.py> [--skip-none]")
        print("")
        print("  --skip-none   hide '# val: None' lines (e.g. from f.write() calls)")
        sys.exit(1)

    print(run_and_annotate(args[0], skip_none=skip_none))
