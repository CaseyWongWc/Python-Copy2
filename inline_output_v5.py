"""
inline_output_v5.py
Casey's phone-shell-fix v5 — Jupyter-style + ZyBooks section log!

What's new in v5 (vs v3):
- Everything v3 does (inline print/expression annotation) is unchanged.
- NEW: Use a standalone  ;  line to divide your file into problem sections.
  Each section between  ;  markers gets its own timestamped entry in the log.
  The whole file still runs as one (so imports/variables carry through), but
  the log is split per-section so each ZyBooks problem is stored cleanly.
- NEW: Optional `append_to` log file (e.g. zy_log.py) that only ever grows —
  your history is never overwritten.
- NEW: Optional `clear_target` — after logging, remove every section that ends
  with a  ;  line (i.e. "done" sections), keeping only the last/current one.
  Great for moving to the next problem without losing any work.

Workflow:

    goog.py                          zy_log.py (grows automatically)
    ──────────────────────           ────────────────────────────────
    from Helpers.helpings import *
    x = 10                           # ===== 2026-05-01 14:00 | goog.py #1 =====
    x                                from Helpers.helpings import *
    print("done")                    x = 10
    ;        ← "commit" marker       x
    y = 99   ← next problem          # val: 10
    y                                print("done")
                                     # out: done
                                     # ===== end =====

                                     # ===== 2026-05-01 14:00 | goog.py #2 =====
                                     y = 99
                                     y
                                     # val: 99
                                     # ===== end =====

Rules / notes:
- SECTION_DELIM (default ";") must be the ONLY non-whitespace character on a line.
- A bare ";" is valid Python (empty statement), so the file runs without errors.
- Sections are separated for LOGGING only — execution is still one run, so
  variables/imports from earlier sections are visible in later ones.
- If `append_to` is None, the file is still annotated inline (like plain v3).
- If `clear_target` is True, all sections that end with a  ;  line are removed
  after logging; the last (current) section stays for continued editing.
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
SECTION_DELIM = ";"        # a line whose stripped content is exactly this


# ---------- helpers (identical to v3) ----------

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


# ---------- NEW v5: section splitting ----------

def _is_delim_line(line: str) -> bool:
    return line.strip() == SECTION_DELIM


def _mask_delimiters(src: str) -> tuple[str, set[int]]:
    """
    Replace standalone  ;  lines with blank lines so Python can parse/run the
    file without a SyntaxError.  Returns (masked_src, set_of_delim_line_numbers).
    Line numbers are 1-indexed to match AST lineno convention.
    """
    delim_lines: set[int] = set()
    out: list[str] = []
    for lineno, line in enumerate(src.splitlines(keepends=True), start=1):
        if _is_delim_line(line):
            delim_lines.add(lineno)
            out.append("\n")          # blank line keeps all other line numbers intact
        else:
            out.append(line)
    return "".join(out), delim_lines


def _split_annotated_into_sections(annotated_lines: list[str]) -> list[list[str]]:
    """
    Split the annotated line list on restored  ;  lines.
    The  ;  lines are delimiters only — they don't appear in the log sections.
    Empty sections are dropped.
    """
    sections: list[list[str]] = []
    current: list[str] = []
    for line in annotated_lines:
        if _is_delim_line(line):
            if any(l.strip() for l in current):
                sections.append(current)
            current = []
        else:
            current.append(line)
    if any(l.strip() for l in current):
        sections.append(current)
    return sections


def _append_sections_to_log(
    log_path: Path,
    sections: list[list[str]],
    source_name: str,
) -> None:
    """Append each section as its own timestamped entry."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_path.open("a", encoding="utf-8") as f:
        for i, section in enumerate(sections, start=1):
            label = f"{source_name} #{i}" if len(sections) > 1 else source_name
            f.write(f"\n# ===== {timestamp} | {label} =====\n")
            f.write("\n".join(section).rstrip("\n") + "\n")
            f.write("# ===== end =====\n")


# ---------- main entry point ----------

def run_and_annotate(
    path: str,
    skip_none: bool = False,
    append_to: str | None = None,
    clear_target: bool = False,
    clear_header: str = "",
) -> str:
    """
    Run `path`, inline-annotate it (same as v3), then:
      - Split the annotated result on standalone  ;  lines into sections.
      - Append each section as its own entry in `append_to` (the log).
      - If `clear_target` is True, remove all "done" sections (those that were
        followed by a  ;  line) from the target, keeping only the last section
        so you can keep working on the current problem.

    Parameters
    ----------
    path          : target .py file to run and annotate
    skip_none     : hide '# val: None' lines
    append_to     : cumulative log file path (created if missing); None = no log
    clear_target  : remove completed sections from the target after logging
    clear_header  : prepended to whatever remains after clearing
    """
    global skip_none_flag
    skip_none_flag = bool(skip_none)

    src_path = Path(path)
    original = src_path.read_text()
    cleaned = _strip_old_annotations(original)

    # Mask ; delimiter lines with blank lines so Python won't choke on them.
    # We track which 1-indexed line numbers they occupied so we can restore them
    # in the final output and split on them for logging.
    runnable, delim_linenos = _mask_delimiters(cleaned)
    src_path.write_text(runnable)

    bare_lines = _find_bare_expr_lines(runnable, skip_none=skip_none)
    shim = _build_shim(src_path, bare_lines)
    out_map, val_map, err_lines = _run_shim(src_path, shim)

    if not out_map and not val_map and not err_lines:
        src_path.write_text(original)   # restore with original ; lines
        return "No output captured. (File ran clean with no prints/expressions, or fatal error before any output.)"

    # Build annotated lines, restoring ; where blank-line masks were.
    # We iterate over the *runnable* (masked) source for line numbers, but
    # re-insert ; wherever the original had a delimiter.
    new_lines = []
    for idx, line in enumerate(runnable.splitlines(), start=1):
        if idx in delim_linenos:
            new_lines.append(";")      # restore the visual separator
        else:
            new_lines.append(line)
            indent = re.match(r"\s*", line).group(0)
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

    # --- v5: split on ; positions and log each section ---

    log_note = ""
    sections = _split_annotated_into_sections(new_lines)

    if append_to is not None:
        log_path = Path(append_to)
        _append_sections_to_log(log_path, sections, src_path.name)
        n = len(sections)
        log_note = f"  Logged {n} section{'s' if n != 1 else ''} → {log_path.name}."

    if clear_target:
        # Keep only the last section (current work-in-progress).
        # Strip its annotations so it's a clean slate for the next run.
        last_section_raw = sections[-1] if sections else []
        last_clean = _strip_old_annotations("\n".join(last_section_raw))
        kept = (clear_header + "\n" if clear_header else "") + last_clean
        src_path.write_text(kept.rstrip("\n") + "\n")
        cleared = len(sections) - 1
        log_note += f"  Cleared {cleared} completed section{'s' if cleared != 1 else ''} from {src_path.name}."

    # Summary
    counts = []
    if out_map:
        counts.append(f"{sum(len(v) for v in out_map.values())} print outputs")
    if val_map:
        counts.append(f"{sum(len(v) for v in val_map.values())} expression values")
    summary = ", ".join(counts) if counts else "no output"
    return f"Annotated {src_path.name} → {summary}.{log_note}"


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
        print("Usage: python inline_output_v5.py <file.py> [--append=log.py] [--clear] [--skip-none]")
        sys.exit(1)

    print(run_and_annotate(args[0], skip_none=skip_none, append_to=append_to, clear_target=clear_target))
