"""
inline_output.py
Casey's phone-shell-fix: run a .py file and rewrite it with each print()'s
output inlined as a #comment right after the print line.

Usage (in Replit, on a fresh file):
    python inline_output.py your_file.py

Or import + call:
    from inline_output import run_and_annotate
    run_and_annotate("your_file.py")

What you get:
    BEFORE:                  AFTER:
    print(1)                 print(1)
    print("hi")              # 1
                             print("hi")
                             # hi

Notes:
- Runs your file in a subprocess so prints really execute (catches f-strings,
  variables, loops, everything).
- Multi-line outputs are wrapped: each output line becomes its own #comment.
- Re-running on an already-annotated file: it strips the old #out: comments
  first so you don't get layered comments.
- Errors/tracebacks ARE captured and inlined as #!err: comments.
"""

import re
import subprocess
import sys
from pathlib import Path

OUT_PREFIX = "# out:"
ERR_PREFIX = "# !err:"


def _strip_old_annotations(src: str) -> str:
    """Remove lines that start with our annotation prefixes (after whitespace)."""
    keep = []
    for line in src.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith(OUT_PREFIX) or stripped.startswith(ERR_PREFIX):
            continue
        keep.append(line)
    return "".join(keep)


def _run_with_line_tags(src_path: Path) -> dict:
    """
    Run the user's file with a shim that prefixes every printed line with
    its source line number, so we can scatter outputs back to the right place.
    Returns {line_number: [output_str, ...]}
    """
    # Shim: monkey-patch print() to also stamp the caller's line number.
    shim = (
        "import sys, builtins, inspect\n"
        "_orig_print = builtins.print\n"
        "def _tagged_print(*args, **kwargs):\n"
        "    frame = inspect.currentframe().f_back\n"
        "    lineno = frame.f_lineno\n"
        "    import io\n"
        "    buf = io.StringIO()\n"
        "    kwargs2 = dict(kwargs); kwargs2['file'] = buf; kwargs2.pop('flush', None)\n"
        "    _orig_print(*args, **kwargs2)\n"
        "    text = buf.getvalue().rstrip('\\n')\n"
        "    for piece in text.split('\\n'):\n"
        "        sys.stdout.write(f'__INLINE__{lineno}__{piece}\\n')\n"
        "    sys.stdout.flush()\n"
        "builtins.print = _tagged_print\n"
        f"exec(compile(open(r'{src_path}').read(), r'{src_path}', 'exec'))\n"
    )

    proc = subprocess.run(
        [sys.executable, "-c", shim],
        capture_output=True,
        text=True,
        timeout=30,
    )

    outputs: dict[int, list[str]] = {}
    for line in proc.stdout.splitlines():
        m = re.match(r"__INLINE__(\d+)__(.*)", line)
        if m:
            ln = int(m.group(1))
            outputs.setdefault(ln, []).append(m.group(2))

    if proc.returncode != 0 and proc.stderr.strip():
        # Stuff full traceback under line 0 so we tack it at the bottom.
        outputs.setdefault(0, []).append("--- ERROR ---")
        for el in proc.stderr.splitlines():
            outputs[0].append(el)

    return outputs


def run_and_annotate(path: str) -> str:
    src_path = Path(path)
    original = src_path.read_text()
    cleaned = _strip_old_annotations(original)
    src_path.write_text(cleaned)

    outputs = _run_with_line_tags(src_path)

    if not outputs:
        # Nothing printed; restore original and bail.
        src_path.write_text(original)
        return "No print() output captured. (File ran clean with no prints, or had a fatal error before any print.)"

    # Re-read cleaned, splice in #out lines AFTER each line that produced output.
    new_lines = []
    for idx, line in enumerate(cleaned.splitlines(), start=1):
        new_lines.append(line)
        if idx in outputs:
            indent = re.match(r"\s*", line).group(0)
            for out_line in outputs[idx]:
                new_lines.append(f"{indent}{OUT_PREFIX} {out_line}")

    # Tack errors at bottom, if any.
    if 0 in outputs:
        new_lines.append("")
        for el in outputs[0]:
            new_lines.append(f"{ERR_PREFIX} {el}")

    final = "\n".join(new_lines) + "\n"
    src_path.write_text(final)
    return f"✅ Annotated {src_path.name}. Open the file to see prints inlined as # out: comments."


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inline_output.py <your_file.py>")
        sys.exit(1)
    print(run_and_annotate(sys.argv[1]))
