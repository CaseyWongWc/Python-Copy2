"""
Smoke test for the v6 friendly-indent + tab-normalize features.

Usage: python sandbox/_smoke_test_indent_fix.py

Covers:
  (a) leading TAB indentation on a `with Scratch:` body — auto-normalized
      to 4 spaces, runs cleanly, no error annotations.
  (b) leading non-breaking-space (U+00A0) indentation — same; auto-fixed.
  (c) mismatched indent (`    x = 1` then `   y = 2`) — produces a
      `# !err: IndentationError on line N` friendly message that names
      BOTH lines and their indent counts. Shim is NOT invoked (no raw
      Python traceback in the output).
  (d) missing indent after `:` — `# !err:` says "this line needs to be
      indented" and points at the colon line.
  (e) plain SyntaxError (e.g. unmatched paren) — gets a friendly
      `# !err: SyntaxError on line N: ...` message instead of a
      raw traceback.
  (f) tab inside a string literal (`print("a\\tb")`) — string content
      is preserved byte-exact, NOT expanded to 4 spaces.
"""
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from inline_output_v6 import run_and_annotate  # noqa: E402


def _run_case(label: str, source: str, checks):
    """Write `source` to a temp notebook, run it, and apply each check.
    `checks` is a list of (description, predicate) where predicate takes
    the annotated output string and returns True/False.
    """
    tmpdir = Path(tempfile.mkdtemp(prefix="v6_indent_"))
    try:
        notebook = tmpdir / "nb.py"
        notebook.write_text(source)
        run_and_annotate(str(notebook), files_dir=tmpdir / "files")
        annotated = notebook.read_text()
        for desc, pred in checks:
            assert pred(annotated), (
                f"\n[{label}] check failed: {desc}\n"
                f"--- annotated output ---\n{annotated}\n--- end ---"
            )
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# (a) tabs on a Scratch body — should run cleanly
TAB_SOURCE = (
    "with Scratch as a:\n"
    "\tx = 5\n"
    "\ty = 7\n"
    "\ttotal = x + y\n"
    "\n"
    "a.total\n"
)
_run_case(
    "(a) leading tab indentation",
    TAB_SOURCE,
    [
        ("a.total annotated as 12", lambda s: "# val: 12" in s),
        ("no IndentationError leaked", lambda s: "IndentationError" not in s),
        ("no raw traceback leaked", lambda s: "Traceback" not in s),
    ],
)
print("✅ (a) leading-tab indentation auto-fixed and ran")

# (b) non-breaking spaces in indentation
NBSP_SOURCE = (
    "with Scratch as a:\n"
    "\u00a0\u00a0\u00a0\u00a0n = 99\n"
    "\n"
    "a.n\n"
)
_run_case(
    "(b) NBSP indentation",
    NBSP_SOURCE,
    [
        ("a.n annotated as 99", lambda s: "# val: 99" in s),
        ("no IndentationError leaked", lambda s: "IndentationError" not in s),
    ],
)
print("✅ (b) non-breaking-space indentation auto-fixed and ran")

# (c) mismatched indent — friendly error
BAD_INDENT_SOURCE = (
    "def foo():\n"
    "    x = 1\n"
    "   y = 2\n"
)
_run_case(
    "(c) mismatched indent",
    BAD_INDENT_SOURCE,
    [
        ("friendly IndentationError emitted",
         lambda s: "# !err: IndentationError on line 3" in s),
        ("mentions previous line's indent",
         lambda s: "line 2" in s and ("indented 4" in s or "indent: 4" in s)),
        ("no raw Python traceback",
         lambda s: "Traceback (most recent call last)" not in s),
    ],
)
print("✅ (c) mismatched indent produced friendly multi-line error")

# (d) missing indent after `:`
MISSING_INDENT_SOURCE = (
    "if True:\n"
    "print('hi')\n"
)
_run_case(
    "(d) missing indent after colon",
    MISSING_INDENT_SOURCE,
    [
        ("friendly IndentationError emitted",
         lambda s: "# !err: IndentationError on line 2" in s),
        ("mentions needs-to-be-indented",
         lambda s: "needs to be indented" in s),
        ("suggests the right indent count",
         lambda s: "try 4 spaces" in s),
    ],
)
print("✅ (d) missing-indent-after-colon explained nicely")

# (e) plain SyntaxError — unmatched paren
SYNTAX_ERR_SOURCE = (
    "x = 1\n"
    "y = (1 + 2\n"
    "z = 3\n"
)
_run_case(
    "(e) plain SyntaxError",
    SYNTAX_ERR_SOURCE,
    [
        ("friendly SyntaxError emitted",
         lambda s: "# !err: SyntaxError on line" in s),
        ("no raw Python traceback",
         lambda s: "Traceback (most recent call last)" not in s),
    ],
)
print("✅ (e) plain SyntaxError got a friendly one-line message")

# (f) tab inside a string literal — must be preserved
# msg content (35 chars): "line1\n" (6) + "\t" (1) + "indented inside string\n"
# (23) + "line3" (5) = 35. If the leading tab on line 2 of the multi-line
# string got expanded to 4 spaces, len would be 38 instead.
STRING_TAB_SOURCE = (
    'print("a\\tb")\n'
    'msg = """line1\n'
    '\tindented inside string\n'
    'line3"""\n'
    'len(msg)\n'
)
_run_case(
    "(f) tab in string literal preserved",
    STRING_TAB_SOURCE,
    [
        ("print output contains a real tab",
         lambda s: "# out: a\tb" in s),
        ("string length unchanged at 35 (tab preserved as 1 char)",
         lambda s: "# val: 35" in s),
        ("length is NOT 38 (would mean tab got expanded)",
         lambda s: "# val: 38" not in s),
    ],
)
print("✅ (f) tab inside string literal stayed byte-exact")

print()
print("✅ all friendly-indent / whitespace-normalize smoke-test cases passed")
