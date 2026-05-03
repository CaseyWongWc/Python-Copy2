"""
Smoke test for Task #13: clean-save, scratch capture, reversed save+run
header shape, and the RUN-hang EOF fix.

Usage: python sandbox/_smoke_test_task13.py

Covers:
  (a) reversed save+run header `with Scratch: "name.py"` writes the body
      to disk AND runs it sandboxed. Body annotations work normally.
  (b) reversed save+run with capture: `with Scratch as a: "name.py"`
      binds `a.x` from the body's locals (same as forward shape).
  (c) clean-save: a body with `# in:` / `# out:` / `# val:` / `# !err:`
      lines lands on disk without those lines. Iterated runs don't
      grow the saved file.
  (d) capture onto `a`: `with Scratch as a:` exposes `a.out` (list of
      printed lines), `a.outs` (joined string), and `a.err` (stderr
      lines). `print(a.outs)` in a follow-up line round-trips the
      block's output verbatim.
  (e) RUN-hang EOF: `with RUN:` whose body calls `input()` with NO
      `# in:` queued does NOT hang — it sees EOFError and exits with
      a non-zero code, surfaced as `# !err: subprocess exited with code N`.
"""
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from inline_output_v6 import run_and_annotate  # noqa: E402


def _run_case(label: str, source: str, checks, files_dir_inspector=None):
    tmpdir = Path(tempfile.mkdtemp(prefix="v6_t13_"))
    try:
        notebook = tmpdir / "nb.py"
        notebook.write_text(source)
        files_dir = tmpdir / "files"
        run_and_annotate(str(notebook), files_dir=files_dir)
        annotated = notebook.read_text()
        for desc, pred in checks:
            assert pred(annotated), (
                f"\n[{label}] check failed: {desc}\n"
                f"--- annotated ---\n{annotated}\n--- end ---"
            )
        if files_dir_inspector is not None:
            files_dir_inspector(files_dir, annotated)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# (a) reversed save+run shape — bare colon form
REV_SOURCE = (
    'with Scratch: "rev.py"\n'
    "    x = 5\n"
    "    y = 7\n"
    "    print(x + y)\n"
    "    x + y\n"
)


def _check_a(files_dir, annotated):
    saved = (files_dir / "rev.py").read_text()
    assert "print(x + y)" in saved, (
        f"(a) saved file missing body: {saved!r}"
    )
    assert "with Scratch" not in saved, (
        f"(a) saved file should not contain header: {saved!r}"
    )


_run_case(
    "(a) reversed `with Scratch: \"rev.py\"`",
    REV_SOURCE,
    [
        ("body printed 12", lambda s: "# out: 12" in s),
        ("bare expr annotated as 12", lambda s: "# val: 12" in s),
        ("no syntax error leaked", lambda s: "SyntaxError" not in s),
    ],
    files_dir_inspector=_check_a,
)
print("✅ (a) reversed `with Scratch: \"name.py\"` saved + ran")


# (b) reversed save+run with capture
REV_CAP_SOURCE = (
    'with Scratch as a: "rev2.py"\n'
    "    x = 99\n"
    "    y = 1\n"
    "\n"
    "a.x\n"
    "a.y\n"
)
_run_case(
    "(b) reversed `with Scratch as a: \"rev2.py\"`",
    REV_CAP_SOURCE,
    [
        ("a.x annotated as 99", lambda s: "# val: 99" in s),
        ("a.y annotated as 1", lambda s: "# val: 1" in s),
    ],
    files_dir_inspector=lambda fd, _: (
        (fd / "rev2.py").read_text().__contains__("x = 99")
        or (_ for _ in ()).throw(AssertionError("(b) saved file missing"))
    ),
)
print("✅ (b) reversed `with Scratch as a: \"name.py\"` captured locals")


# (c) clean-save: stale annotations get stripped before write
DIRTY_SOURCE = (
    'with "dirty.py" as Scratch:\n'
    "    name = input()\n"
    "    # in: Casey\n"
    "    print('hi', name)\n"
    "    # out: hi Casey\n"
    "    1 + 1\n"
    "    # val: 2\n"
    "\n"
    "1 + 1\n"
)


def _check_c(files_dir, annotated):
    saved = (files_dir / "dirty.py").read_text()
    assert "# in:" not in saved, f"(c) `# in:` leaked into saved file: {saved!r}"
    assert "# out:" not in saved, f"(c) `# out:` leaked: {saved!r}"
    assert "# val:" not in saved, f"(c) `# val:` leaked: {saved!r}"
    assert "name = input()" in saved, f"(c) real code missing: {saved!r}"
    assert "print('hi', name)" in saved, f"(c) real code missing: {saved!r}"


_run_case(
    "(c) clean-save strips notebook annotations",
    DIRTY_SOURCE,
    [
        ("block ran with queued input", lambda s: "# out: hi Casey" in s),
    ],
    files_dir_inspector=_check_c,
)
print("✅ (c) clean-save strips `# in:` / `# out:` / `# val:` / `# !err:`")


# (d) capture onto `a`: a.out, a.outs, a.err
CAP_SOURCE = (
    "import sys\n"
    "with Scratch as a:\n"
    "    print('hello')\n"
    "    print('world')\n"
    "    sys.stderr.write('boom\\n')\n"
    "\n"
    "a.out\n"
    "a.outs\n"
    "len(a.err)\n"
    "print(a.outs)\n"
)
_run_case(
    "(d) capture onto `a`",
    CAP_SOURCE,
    [
        ("a.out is the two-line list",
         lambda s: "# val: ['hello', 'world']" in s),
        ("a.outs is joined string",
         lambda s: "# val: hello" in s and "# val: world" in s),
        ("a.err captured the stderr write",
         lambda s: "# val: 1" in s),
        ("print(a.outs) round-trips both lines",
         lambda s: "# out: hello" in s and "# out: world" in s),
    ],
)
print("✅ (d) `with Scratch as a:` captured a.out / a.outs / a.err")


# (e) RUN EOF: input() with no queue must not hang
RUN_EOF_SOURCE = (
    "with RUN:\n"
    "    name = input()\n"
    "    print('got', name)\n"
)
_run_case(
    "(e) RUN with empty input queue does not hang",
    RUN_EOF_SOURCE,
    [
        ("EOFError surfaces in stderr",
         lambda s: "EOFError" in s),
        ("non-zero exit annotation",
         lambda s: "# !err: subprocess exited with code" in s),
    ],
)
print("✅ (e) `with RUN:` with no `# in:` queue exits cleanly (no hang)")


# (f) a.out filters out prints from helper modules (e.g. setin's mock_input
#     echo). The capture only collects prints whose caller frame is in the
#     notebook file itself, so input echoes from `Helpers/helpings.py:mock_input`
#     (which calls `print(f"{prompt}{value}")`) stay out of `a.out`.
HELPER_FILTER_SOURCE = (
    "import builtins, inspect\n"
    "# Stand-in for `Helpers.helpings.mock_input` — defined in a separate\n"
    "# file and imported, so its frame's filename is NOT the notebook.\n"
    "import os, tempfile\n"
    "_helper_src = '''def mock_input(prompt=\"\"):\n"
    "    print(f\"{prompt}HELPER\")\n"
    "    return \"HELPER\"\n"
    "'''\n"
    "_d = tempfile.mkdtemp()\n"
    "_p = os.path.join(_d, '_h.py')\n"
    "open(_p,'w').write(_helper_src)\n"
    "import sys; sys.path.insert(0, _d)\n"
    "from _h import mock_input\n"
    "builtins.input = mock_input\n"
    "with Scratch as a:\n"
    "    x = input('> ')\n"
    "    print('user-print', x)\n"
    "a.out\n"
)
_run_case(
    "(f) a.out skips prints from helper modules",
    HELPER_FILTER_SOURCE,
    [
        ("a.out has only the user's print, not the helper echo",
         lambda s: "# val: ['user-print HELPER']" in s),
        ("helper echo still shows as `# out:` annotation on input line",
         lambda s: "# out: > HELPER" in s),
    ],
)
print("✅ (f) `a.out` filters out prints from helper modules / mock_input echoes")


print()
print("✅ all task-13 smoke-test cases passed")
