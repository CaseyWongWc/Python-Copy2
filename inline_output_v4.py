"""
inline_output_v4.py
Casey's phone-Python tool — now with auto-save magic comments 💚

What's NEW in v4:
- Magic comments at the top of your file auto-save a copy to the right folder
  AFTER your code runs and gets annotated. Fire and forget.

Magic comments (put any of these on the FIRST 5 lines of your file):

    # zy: 13.1 Item_Produce        → saves to _zybooks/C_13/13.1/Item_Produce.py
    # zy: 13.2 Animal              → saves to _zybooks/C_13/13.2/Animal.py
    # fig: 13.1.1                  → saves to _zybooks/C_13/Figure_13_1_1.py
    # quick: test1                 → saves to scratch/test1.py
    # note: derived_classes        → saves to notes/derived_classes.md
    # save: any/path/here.py       → saves to that exact path (relative to cwd)

Examples:

    # zy: 13.1 Derived_Item
    class Item:
        ...

    → run: python inline_output_v4.py mycode.py
    → annotates mycode.py inline (# out: / # val:)
    → ALSO copies it to _zybooks/C_13/13.1/Derived_Item.py

What you still get from v2/v3:
- print() output → `# out:`
- bare expressions (Jupyter-style) → `# val:`
- errors → `# !err:`

Re-running on an annotated file: strips old annotations first.
"""

import ast
import re
import shutil
import subprocess
import sys
from pathlib import Path

OUT_PREFIX = "# out:"
VAL_PREFIX = "# val:"
ERR_PREFIX = "# !err:"


# ---------- magic comment parsing ----------

def _parse_magic(src: str) -> Path | None:
    """
    Look at the first 5 non-blank lines for a magic comment.
    Returns the destination Path (relative to cwd), or None.
    """
    lines = src.splitlines()
    checked = 0
    for line in lines:
        if checked >= 5:
            break
        stripped = line.strip()
        if not stripped:
            continue
        checked += 1

        # # zy: <section> <name>   →  _zybooks/C_<chap>/<section>/<name>.py
        m = re.match(r"#\s*zy:\s*(\d+)\.(\d+)\s+(\S+)", stripped)
        if m:
            chap, sub, name = m.group(1), m.group(2), m.group(3)
            return Path(f"_zybooks/C_{chap}/{chap}.{sub}/{name}.py")

        # # fig: <chap>.<sub>.<num>  →  _zybooks/C_<chap>/Figure_<chap>_<sub>_<num>.py
        m = re.match(r"#\s*fig:\s*(\d+)\.(\d+)\.(\d+)", stripped)
        if m:
            chap, sub, num = m.group(1), m.group(2), m.group(3)
            return Path(f"_zybooks/C_{chap}/Figure_{chap}_{sub}_{num}.py")

        # # quick: <name>           →  scratch/<name>.py
        m = re.match(r"#\s*quick:\s*(\S+)", stripped)
        if m:
            name = m.group(1)
            if not name.endswith((".py", ".md", ".txt")):
                name += ".py"
            return Path(f"scratch/{name}")

        # # note: <name>            →  notes/<name>.md
        m = re.match(r"#\s*note:\s*(\S+)", stripped)
        if m:
            name = m.group(1)
            if not name.endswith((".md", ".txt")):
                name += ".md"
            return Path(f"notes/{name}")

        # # save: <full/path>       →  <full/path>
        m = re.match(r"#\s*save:\s*(\S+)", stripped)
        if m:
            return Path(m.group(1))

    return None


def _auto_save(src_path: Path) -> str | None:
    """If the source file has a magic comment, copy the (now-annotated) file there."""
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


# ---------- AST helpers (same as v2) ----------

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


def _parse_setin_inputs(src: str) -> list[str]:
    """
    Parse optional #setin directives from the source.

    Supported forms:
      #setin("a", "b")
      #setin a, b, c
      #setin
      # a
      # b
    """
    lines = src.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^\s*#\s*setin\b(.*)$", line)
        if not m:
            continue

        tail = m.group(1).strip()
        if tail:
            # Python-style tuple/list payload
            if tail.startswith("(") or tail.startswith("["):
                try:
                    value = ast.literal_eval(tail)
                    if isinstance(value, (list, tuple)):
                        return [str(v) for v in value]
                    return [str(value)]
                except Exception:
                    pass

            # Fallback CSV-style payload
            parts = [p.strip() for p in tail.split(",")]
            return [p.strip("\"'") for p in parts if p]

        # Block form: consecutive comment lines after #setin
        gathered = []
        j = i + 1
        while j < len(lines):
            comment = re.match(r"^\s*#(.*)$", lines[j])
            if not comment:
                break
            body = comment.group(1).strip()
            if not body:
                break
            if re.match(r"^(zy:|fig:|quick:|note:|save:|setin\b)", body):
                break
            gathered.append(body)
            j += 1
        return gathered

    return []


# ---------- shim builder ----------

skip_none_flag = False


def _build_shim(src_path: Path, bare_lines: set, setin_inputs: list[str]) -> str:
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
        f"_SETIN = {repr(setin_inputs)}\n"
        "if _SETIN:\n"
        "    _setin_iter = iter(_SETIN)\n"
        "    def _setin_input(prompt=''):\n"
        "        frame = inspect.currentframe().f_back\n"
        "        lineno = frame.f_lineno\n"
        "        try:\n"
        "            value = str(next(_setin_iter))\n"
        "        except StopIteration:\n"
        "            raise EOFError('No more #setin inputs')\n"
        "        sys.stdout.write(f'__OUT__{lineno}__{prompt}{value}\\n')\n"
        "        sys.stdout.flush()\n"
        "        return value\n"
        "    builtins.input = _setin_input\n"
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
        f"_BARE_LINES = set({bare_lines_repr})\n"
        "\n"
        f"_src = open(r'{src_path}').read()\n"
        "_tree = ast.parse(_src, filename=r'{path}')\n".replace("{path}", str(src_path)) +
        "\n"
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

def run_and_annotate(path: str, skip_none: bool = False) -> str:
    global skip_none_flag
    skip_none_flag = bool(skip_none)

    src_path = Path(path)
    original = src_path.read_text()
    cleaned = _strip_old_annotations(original)
    src_path.write_text(cleaned)

    bare_lines = _find_bare_expr_lines(cleaned)
    setin_inputs = _parse_setin_inputs(cleaned)
    shim = _build_shim(src_path, bare_lines, setin_inputs)
    out_map, val_map, err_lines = _run_shim(shim)

    # Splice annotations
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
        # Keep error block anchored: avoid drifting downward through trailing blanks.
        while new_lines and new_lines[-1].strip() == "":
            new_lines.pop()
        for el in err_lines:
            new_lines.append(f"{ERR_PREFIX} {el}")

    final = "\n".join(new_lines) + "\n"
    src_path.write_text(final)

    # 🌱 NEW: auto-save based on magic comment
    saved_to = _auto_save(src_path)

    # Summary
    counts = []
    if out_map:
        counts.append(f"{sum(len(v) for v in out_map.values())} print outputs")
    if val_map:
        counts.append(f"{sum(len(v) for v in val_map.values())} expression values")
    summary = ", ".join(counts) if counts else "no output"

    msg = f"✅ Annotated {src_path.name} → {summary}."
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
        print("Usage: python inline_output_v4.py <your_file.py> [--skip-none]")
        print("")
        print("Magic comments (first 5 lines of your file):")
        print("  # zy: 13.1 Item_Produce   → _zybooks/C_13/13.1/Item_Produce.py")
        print("  # fig: 13.1.1             → _zybooks/C_13/Figure_13_1_1.py")
        print("  # quick: test1            → scratch/test1.py")
        print("  # note: derived_classes   → notes/derived_classes.md")
        print("  # save: any/path/here.py  → exact path")
        sys.exit(1)

    print(run_and_annotate(args[0], skip_none=skip_none))
