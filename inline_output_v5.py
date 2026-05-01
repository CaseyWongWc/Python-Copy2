"""
inline_output_v5.py
Casey's phone-shell-fix v5 — Jupyter-style + in-file marker control!

Everything v3 does (inline annotation of print/expressions) is unchanged.
On top of that, two optional markers — placed directly in your .py file —
let you commit finished problems to a log without ever opening main.py.

━━━  SECTION MARKER  (default  ⭐ ) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wrap a finished block between two matching lines:

    from Helpers.helpings import *
    ⭐
    x = 10
    x
    print("done")
    ⭐
    y = 99          ← still in progress, stays in the file
    y

On the next run:
  • the whole file runs (so y can see x if needed)
  • the ⭐ … ⭐ block is annotated, appended to the log, then DELETED
  • everything outside the markers stays in goog.py untouched

You can have multiple ⭐ … ⭐ blocks — each becomes its own log entry.

━━━  CLEAR MARKER  (default  ## ) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Put this anywhere on its own line to nuke the whole file after logging:

    from Helpers.helpings import *
    x = 10
    x
    ##

On the next run:
  • the whole file is annotated and appended to the log as ONE entry
  • goog.py is wiped clean (empty, or just the header if you set one)

━━━  NO MARKERS  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Behaves exactly like v3: output is inlined, nothing is logged or deleted.
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

DEFAULT_SECTION_MARKER = "⭐"
DEFAULT_CLEAR_MARKER   = "##"


# ── helpers (identical to v3) ────────────────────────────────────────────────

def _strip_old_annotations(src: str) -> str:
    keep = []
    for line in src.splitlines(keepends=True):
        s = line.lstrip()
        if s.startswith(OUT_PREFIX) or s.startswith(VAL_PREFIX) or s.startswith(ERR_PREFIX):
            continue
        keep.append(line)
    return "".join(keep)


def _is_print_call(node: ast.expr) -> bool:
    if not isinstance(node, ast.Call):
        return False
    return isinstance(node.func, ast.Name) and node.func.id == "print"


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
            if _is_print_call(node.value) or _is_docstring(node):
                continue
            bare_lines.add(node.lineno)
    return bare_lines


# ── shim (identical to v3) ───────────────────────────────────────────────────

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
        capture_output=True, text=True, timeout=30,
    )
    out_map: dict[int, list[str]] = {}
    val_map: dict[int, list[str]] = {}
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


# ── marker helpers ────────────────────────────────────────────────────────────

def _marker_line(line: str, marker: str) -> bool:
    """True if this line consists solely of the marker token."""
    return line.strip() == marker


def _mask_markers(src: str, section_marker: str, clear_marker: str):
    """
    Replace marker lines with blank lines so Python can parse the file.
    Returns (runnable_src, section_marker_linenos, clear_marker_linenos).
    All line numbers are 1-indexed.
    """
    section_lnos: set[int] = set()
    clear_lnos:   set[int] = set()
    out: list[str] = []
    for lno, line in enumerate(src.splitlines(keepends=True), start=1):
        if _marker_line(line, section_marker):
            section_lnos.add(lno)
            out.append("\n")
        elif _marker_line(line, clear_marker):
            clear_lnos.add(lno)
            out.append("\n")
        else:
            out.append(line)
    return "".join(out), section_lnos, clear_lnos


def _build_annotated_lines(
    runnable: str,
    out_map: dict,
    val_map: dict,
    err_lines: list,
    section_marker_lnos: set,
    clear_marker_lnos: set,
    section_marker: str,
    clear_marker: str,
) -> list[str]:
    """
    Build the annotated line list, restoring marker lines where they were.
    """
    lines = []
    for idx, line in enumerate(runnable.splitlines(), start=1):
        if idx in section_marker_lnos:
            lines.append(section_marker)
            continue
        if idx in clear_marker_lnos:
            lines.append(clear_marker)
            continue
        lines.append(line)
        indent = re.match(r"\s*", line).group(0)
        for out in out_map.get(idx, []):
            lines.append(f"{indent}{OUT_PREFIX} {out}")
        for val in val_map.get(idx, []):
            lines.append(f"{indent}{VAL_PREFIX} {val}")
    if err_lines:
        lines.append("")
        for el in err_lines:
            lines.append(f"{ERR_PREFIX} {el}")
    return lines


def _extract_section_blocks(
    lines: list[str], section_marker: str
) -> tuple[list[list[str]], list[str]]:
    """
    Pull out ⭐…⭐ blocks from lines.
    Returns (blocks, remaining_lines).
    Unmatched opening markers are left in remaining_lines untouched.
    """
    blocks: list[list[str]] = []
    remaining: list[str] = []
    in_block = False
    current: list[str] = []

    for line in lines:
        if _marker_line(line, section_marker):
            if not in_block:
                in_block = True
                current = []
            else:
                if any(l.strip() for l in current):
                    blocks.append(current)
                in_block = False
                current = []
        else:
            if in_block:
                current.append(line)
            else:
                remaining.append(line)

    # Unclosed block → put it back unchanged
    if in_block:
        remaining.append(section_marker)
        remaining.extend(current)

    return blocks, remaining


def _extract_clear_block(
    lines: list[str], clear_marker: str
) -> tuple[bool, list[str]]:
    """
    Check for a clear marker.  If found, return (True, lines_without_marker).
    """
    found = False
    remaining = [l for l in lines if not _marker_line(l, clear_marker) or (found := True) and False]
    # Simpler:
    found = any(_marker_line(l, clear_marker) for l in lines)
    remaining = [l for l in lines if not _marker_line(l, clear_marker)]
    return found, remaining


def _append_to_log(log_path: Path, content_lines: list[str], label: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"\n# ===== {timestamp} | {label} =====\n")
        f.write("\n".join(content_lines).rstrip("\n") + "\n")
        f.write("# ===== end =====\n")


# ── main entry point ──────────────────────────────────────────────────────────

def run_and_annotate(
    path: str,
    skip_none: bool = False,
    append_to: str | None = None,
    section_marker: str = DEFAULT_SECTION_MARKER,
    clear_marker: str = DEFAULT_CLEAR_MARKER,
) -> str:
    """
    Annotate `path` inline (like v3), then handle any in-file markers:

    section_marker (default ⭐)
        Wrap a finished block top-and-bottom.  On run: annotated block is
        appended to `append_to` log, then deleted from the file.

    clear_marker (default ##)
        A single line with this token triggers: annotate everything, append
        the whole file to the log, then wipe the file clean.

    No markers → pure v3 behaviour (annotate in place, nothing logged/deleted).

    Parameters
    ----------
    path            : target .py file
    skip_none       : hide '# val: None' lines
    append_to       : cumulative log file (created if missing); None = no log
    section_marker  : token that wraps done sections (must be alone on its line)
    clear_marker    : token that triggers a full-file log-and-clear
    """
    global skip_none_flag
    skip_none_flag = bool(skip_none)

    src_path = Path(path)
    original = src_path.read_text()
    cleaned  = _strip_old_annotations(original)

    # Replace marker lines with blank lines so the file is valid Python.
    runnable, section_lnos, clear_lnos = _mask_markers(
        cleaned, section_marker, clear_marker
    )
    src_path.write_text(runnable)

    bare_lines = _find_bare_expr_lines(runnable, skip_none=skip_none)
    shim = _build_shim(src_path, bare_lines)
    out_map, val_map, err_lines = _run_shim(src_path, shim)

    if not out_map and not val_map and not err_lines:
        src_path.write_text(original)   # restore with markers intact
        return "No output captured. (File ran clean with no prints/expressions, or fatal error before any output.)"

    annotated = _build_annotated_lines(
        runnable, out_map, val_map, err_lines,
        section_lnos, clear_lnos, section_marker, clear_marker,
    )

    # ── process markers ───────────────────────────────────────────────────────

    log_notes: list[str] = []

    # 1. Section blocks: extract, log, delete
    if section_lnos and append_to is not None:
        blocks, annotated = _extract_section_blocks(annotated, section_marker)
        log_path = Path(append_to)
        for i, block in enumerate(blocks, start=1):
            label = f"{src_path.name} #{i}" if len(blocks) > 1 else src_path.name
            _append_to_log(log_path, block, label)
        if blocks:
            log_notes.append(f"logged {len(blocks)} section(s) → {log_path.name}")
    elif section_lnos:
        # No log destination — just remove the markers visually
        _, annotated = _extract_section_blocks(annotated, section_marker)

    # 2. Clear marker: log everything remaining, then wipe file
    clear_triggered = False
    if clear_lnos:
        found, annotated_no_marker = _extract_clear_block(annotated, clear_marker)
        if found:
            clear_triggered = True
            if append_to is not None:
                log_path = Path(append_to)
                if any(l.strip() for l in annotated_no_marker):
                    _append_to_log(log_path, annotated_no_marker, src_path.name)
                    log_notes.append(f"logged full file → {log_path.name}")
            src_path.write_text("")
            log_notes.append(f"{src_path.name} cleared")

    if not clear_triggered:
        # Write the (possibly section-trimmed) annotated file back
        src_path.write_text("\n".join(annotated) + "\n")

    # ── summary ───────────────────────────────────────────────────────────────

    counts = []
    if out_map:
        counts.append(f"{sum(len(v) for v in out_map.values())} print output(s)")
    if val_map:
        counts.append(f"{sum(len(v) for v in val_map.values())} expression value(s)")
    summary = ", ".join(counts) if counts else "no output"
    note = ("  " + ",  ".join(log_notes)) if log_notes else ""
    return f"Annotated {src_path.name} → {summary}.{note}"


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]
    skip_none = False
    append_to = None
    section_marker = DEFAULT_SECTION_MARKER
    clear_marker   = DEFAULT_CLEAR_MARKER

    for a in list(args):
        if a == "--skip-none":
            skip_none = True; args.remove(a)
        elif a.startswith("--append="):
            append_to = a.split("=", 1)[1]; args.remove(a)
        elif a.startswith("--section="):
            section_marker = a.split("=", 1)[1]; args.remove(a)
        elif a.startswith("--clear="):
            clear_marker = a.split("=", 1)[1]; args.remove(a)

    if not args:
        print("Usage: python inline_output_v5.py <file.py> "
              "[--append=log.py] [--section=⭐] [--clear=##] [--skip-none]")
        sys.exit(1)

    print(run_and_annotate(
        args[0], skip_none=skip_none, append_to=append_to,
        section_marker=section_marker, clear_marker=clear_marker,
    ))
