"""
Smoke test for the v6 friendly-typo-hint feature.

Usage: python sandbox_drafts/_smoke_test_typos.py

Covers:
  (a) NameError on a misspelled BUILTIN (`prnit` → `print`) — a
      `↳ did you mean: print?` hint is appended.
  (b) NameError on a misspelled USER-DEFINED name — hint suggests
      the name the user actually defined earlier in the file.
  (c) NameError where nothing is close enough — NO false hint is
      emitted (silence is better than a wrong suggestion).
  (d) AttributeError on a string method (`"x".uppercas()` →
      `upper`/`zfill`) — hint pulled from `dir(str)`.
  (e) Successful run — hint logic must NOT inject anything when
      there's no traceback at all.
"""
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from inline_output_v6 import run_and_annotate  # noqa: E402


def _run_case(label, source, checks):
    tmpdir = Path(tempfile.mkdtemp(prefix="v6_typos_"))
    try:
        notebook = tmpdir / "nb.py"
        notebook.write_text(source)
        run_and_annotate(str(notebook), files_dir=tmpdir / "files")
        annotated = notebook.read_text()
        for desc, pred in checks:
            assert pred(annotated), (
                f"\n[{label}] check failed: {desc}\n"
                f"--- annotated ---\n{annotated}\n--- end ---"
            )
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# (a) Misspelled builtin
_run_case(
    "(a) NameError on misspelled builtin (prnit)",
    'prnit("hi")\n',
    [
        ("NameError reported in traceback",
         lambda s: "NameError" in s and "prnit" in s),
        ("hint suggests `print`",
         lambda s: "did you mean" in s and "print" in s),
    ],
)
print("✅ (a) misspelled builtin → suggests `print`")


# (b) Misspelled user-defined name
_run_case(
    "(b) NameError on misspelled user var",
    'longest_score = 99\n'
    'print(longest_scor)\n',
    [
        ("NameError reported", lambda s: "NameError" in s),
        ("hint suggests the user's actual name",
         lambda s: "did you mean" in s and "longest_score" in s),
    ],
)
print("✅ (b) misspelled user-defined name → suggests user's actual var")


# (c) Nothing remotely close — no false hint
_run_case(
    "(c) NameError with no close match",
    'xyzzy_qqqq_zzzz\n',
    [
        ("NameError reported", lambda s: "NameError" in s),
        ("NO `did you mean` hint emitted",
         lambda s: "did you mean" not in s),
    ],
)
print("✅ (c) NameError with no close match → silent (no false hint)")


# (d) Misspelled string method
_run_case(
    "(d) AttributeError on str method (uppercas)",
    '"hello".uppercas()\n',
    [
        ("AttributeError reported", lambda s: "AttributeError" in s),
        ("hint suggests `upper`",
         lambda s: "did you mean" in s and "upper" in s),
    ],
)
print("✅ (d) misspelled str method → suggests `upper`")


# (e) Successful run — no hint injection
_run_case(
    "(e) successful run, no hint expected",
    'x = 5\n'
    'y = 7\n'
    'x + y\n',
    [
        ("expression value annotated", lambda s: "# val: 12" in s),
        ("NO `did you mean` hint", lambda s: "did you mean" not in s),
        ("NO error annotation",
         lambda s: "NameError" not in s and "AttributeError" not in s),
    ],
)
print("✅ (e) clean run leaves no spurious hints")


print()
print("✅ all friendly-typo-hint smoke-test cases passed")
