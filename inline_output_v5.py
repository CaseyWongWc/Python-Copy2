"""
inline_output_v5.py
Casey's phone-shell-fix v5 — Jupyter-style + ZyBooks append log!

What's new in v5 (vs v3):
- Everything v3 does (inline print/expression annotation) is unchanged.
- NEW: After annotating your file, optionally append the annotated snapshot
  to a "log" file (e.g. zy_log.py).  Over time this log builds up a history
  of every ZyBooks problem you've solved, so autocomplete keeps full context
  without you having to triple-tick anything.
- NEW: Optional `clear_target` flag — wipe the target file clean (except a
  configurable header line) before running, so each problem starts fresh.
- NEW: `append_separator` in the log marks each entry with a timestamp and
  the source filename, making it easy to scroll back through past problems.

Typical main.py usage:

    from inline_output_v5 import run_and_annotate

    run_and_annotate(
        path        = "goog.py",        # file you are actively working in
        append_to   = "zy_log.py",      # cumulative notebook log
        clear_target = False,           # set True to blank goog.py after logging
    )

Log file format (zy_log.py grows over time):

    # ===== 2026-05-01 14:22:03 | goog.py =====
    x = 5
    x
    # val: 5
    # ===== end =====

Rules / notes:
- If `append_to` is None, v5 behaves exactly like v3 (no log written).
- The log is ONLY appended to, never overwritten — your history is safe.
- Re-running on an already-annotated file still strips old annotations first
  (same as v3).
- If `clear_target` is True the target is reset to just an import line
  (configurable via `clear_header`) AFTER the annotated snapshot is logged.
"""

import ast
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

OUT_PREFIX = "# out:"
VAL_PREFIX = "# val:"
ERR_PREFIX = "# !err:"


# ---------- helpers (identical to v3) ----------

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


def _is_print_call(node: ast.expr) -> bool:
    if not isinstance(node, ast.Call):
        return False
    func = node.func
    return isinstance(func, ast.Name) and func.id == "print"


def _is_docstring(node: ast.Expr) -> bool:
    return isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)


def _find_bare_expr_lines(src: str, skip_none: bool) -> set:
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


# ---------- shim builder (identical to v3) ----------

skip_none_flag = False


def _build_shim(src_path: Path, bare_lines: set) -> str:
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
        "_tree = ast.parse(_src, filename=r'{path}')\n".replace("{path}", str(src_path))
        + "\n"
        "import builtins as _bi\n"
        "_bi._show_val = _show_val\n"
        "\n"
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
        "_tree = _Rewriter().visit(_tree)\n"
        "ast.fix_missing_locations(_tree)\n"
        f"_code = compile(_tree, r'{src_path}', 'exec')\n"
        "exec(_code, {'__name__': '__main__', '__file__': r'" + str(src_path) + "'})\n"
    )


def _run_shim(src_path: Path, shim_src: str) -> tuple:
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


# ---------- NEW v5 helper: append to log ----------

def _append_to_log(log_path: Path, annotated_src: str, source_name: str) -> None:
    """
    Append a timestamped snapshot of the annotated source to the log file.
    Creates the log file if it doesn't exist yet.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    separator_open  = f"# ===== {timestamp} | {source_name} =====\n"
    separator_close = "# ===== end =====\n"

    with log_path.open("a", encoding="utf-8") as f:
        f.write("\n")
        f.write(separator_open)
        f.write(annotated_src.rstrip("\n") + "\n")
        f.write(separator_close)


# ---------- main entry point ----------

def run_and_annotate(
    path: str,
    skip_none: bool = False,
    append_to: str | None = None,
    clear_target: bool = False,
    clear_header: str = "",
) -> str:
    """
    Run `path`, inline-annotate it (same as v3), then optionally:
      - append the annotated snapshot to `append_to` (a log / ZyBooks notebook)
      - reset `path` to `clear_header` so you get a clean slate for the next problem

    Parameters
    ----------
    path          : target .py file to run and annotate
    skip_none     : hide '# val: None' lines (e.g. from file.write() calls)
    append_to     : if given, append annotated snapshot here (creates file if needed)
    clear_target  : if True, reset the target file to `clear_header` after logging
    clear_header  : what to leave in the target file after clearing
                    (default: empty string, i.e. blank file)
    """
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

    # --- v5 additions ---

    log_note = ""
    if append_to is not None:
        log_path = Path(append_to)
        _append_to_log(log_path, final, src_path.name)
        log_note = f"  Appended to {log_path.name}."

    if clear_target:
        src_path.write_text(clear_header + ("\n" if clear_header else ""))
        log_note += f"  {src_path.name} cleared."

    # --- summary ---

    counts = []
    if out_map:
        counts.append(f"{sum(len(v) for v in out_map.values())} print outputs")
    if val_map:
        counts.append(f"{sum(len(v) for v in val_map.values())} expression values")
    summary = ", ".join(counts) if counts else "no output"
    return (
        f"Annotated {src_path.name} → {summary}. Open the file to see them inlined.{log_note}"
    )


# ---------- CLI ----------

if __name__ == "__main__":
    args = sys.argv[1:]
    skip_none = False
    append_to = None
    clear_target = False

    if "--skip-none" in args:
        skip_none = True
        args.remove("--skip-none")
    if "--clear" in args:
        clear_target = True
        args.remove("--clear")
    for a in list(args):
        if a.startswith("--append="):
            append_to = a.split("=", 1)[1]
            args.remove(a)

    if not args:
        print("Usage: python inline_output_v5.py <your_file.py> [--append=log.py] [--clear] [--skip-none]")
        sys.exit(1)

    print(run_and_annotate(args[0], skip_none=skip_none, append_to=append_to, clear_target=clear_target))
