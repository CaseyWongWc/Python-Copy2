"""
Ad-hoc smoke test for the `with "X" as RUN:` save-and-fresh-subprocess-run
combo (task 9).

Usage: python sandbox/_smoke_test_save_run_run.py

Builds a small notebook in a temp dir, runs it through
`run_and_annotate`, and asserts the resulting annotations cover the
seven cases below:

  (a) save AND run: file lands on disk verbatim, body's print() shows up
      as `# out:` under the LAST non-blank body line
  (b) process isolation: an outer-scope variable is INVISIBLE to the
      subprocess (NameError + non-zero exit annotation), AND the
      traceback path points at the user-saved file (e.g.
      `File "isolation.py"`) — NOT a `.run_blocks/...` temp file
  (c) `with "X" as RUN: -V` passes args to python3
  (d) docstring containing a fake save+RUN header is left alone
  (e) body invalid Python -> `# !err: SyntaxError` AND the file is NOT
      written, AND the rest of the notebook still runs
  (f) comma form `with "X", RUN:` is accepted (file written, body run)
  (g) outer `# in:` queue is NOT shared with the subprocess; an inner
      `# in:` inside the body feeds the subprocess's stdin
"""
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from inline_output_v6 import run_and_annotate  # noqa: E402


NOTEBOOK = '''\
"""
Docstring with a fake header — should NOT be processed:

    with "should_not_exist.py" as RUN:
        print("docstring contents — must not run")
"""

# (a) save + run, body's print(n3) lands as # out: under the LAST line
with "verbatim_run.py" as RUN:
    n1 = 5
    n2 = 7.5
    n3 = n1 + n2
    print(n3)

# (b) process isolation: outer var is invisible to the subprocess
outer_var = "you can't see me"
with "isolation.py" as RUN:
    print(outer_var)

# (c) inline argv: -V prints the Python version
with "vflag.py" as RUN: -V
    pass

# (e) body invalid Python -> # !err: SyntaxError, file NOT written
with "bad_syntax_run.py" as RUN:
    this is not valid python at all !!!

# After the bad block, the rest of the notebook MUST keep running.
recovered = "yes"
recovered

# (f) comma form: `with "X", RUN:`
with "comma_form_run.py", RUN:
    print("comma form ran")

# An OUTER `# in:` queue value the subprocess must NOT see.
# in: 999
with "stdin_iso.py" as RUN:
    # in: 42
    n = int(input())
    print("got:", n)
'''


def main():
    tmp = Path(tempfile.mkdtemp(prefix="save_run_run_smoke_"))
    try:
        nb = tmp / "nb.py"
        nb.write_text(NOTEBOOK)
        files_dir = tmp / "files"
        msg = run_and_annotate(str(nb), files_dir=files_dir)
        print(msg)
        print("---- annotated ----")
        result = nb.read_text()
        print(result)
        print("---- end ----")

        # (a) verbatim file content + body executed in fresh subprocess
        verbatim_path = files_dir / "verbatim_run.py"
        assert verbatim_path.is_file(), (
            "case (a) failed: sandbox/files/verbatim_run.py was not written"
        )
        verbatim = verbatim_path.read_text()
        for needle in ("n1 = 5", "n2 = 7.5", "n3 = n1 + n2", "print(n3)"):
            assert needle in verbatim, (
                f"case (a) failed: missing `{needle}` in verbatim_run.py"
            )
        assert "# out: 12.5" in result, (
            "case (a) failed: body's print(n3) didn't run in subprocess"
        )

        # (b) process isolation: NameError on `outer_var` + non-zero exit
        assert "NameError" in result and "outer_var" in result, (
            "case (b) failed: expected NameError on `outer_var` in subprocess"
        )
        assert "# !err: subprocess exited with code" in result, (
            "case (b) failed: expected non-zero exit annotation"
        )
        # Traceback should reference the user-saved file path, NOT the
        # `.run_blocks/...` throwaway temp. Python 3.11+ normalizes the
        # script argument to an absolute path in tracebacks, so we
        # assert on the absolute path that ends in the user-typed name.
        expected_path = str((files_dir / "isolation.py").resolve())
        assert f'File "{expected_path}"' in result, (
            "case (b) failed: traceback should point at the saved file "
            f"`{expected_path}`, but it doesn't.\nGot:\n{result}"
        )
        assert ".run_blocks" not in result, (
            "case (b) failed: traceback (or another annotation) referenced "
            "a `.run_blocks/...` temp path; save+RUN must run the saved "
            "file directly"
        )

        # (c) -V flag returns "Python 3.x.y" (lands on stdout or stderr
        # depending on the Python version)
        assert "# out: Python 3" in result or "# err: Python 3" in result, (
            "case (c) failed: expected Python version string from -V"
        )

        # (d) docstring contents must not be annotated and no file written
        docstring_path = files_dir / "should_not_exist.py"
        assert not docstring_path.exists(), (
            "case (d) failed: docstring's fake header was processed"
        )
        assert "# out: docstring contents" not in result, (
            "case (d) failed: docstring `with ... as RUN:` was executed"
        )

        # (e) syntax error: NO file write, # !err: annotation present
        bad_path = files_dir / "bad_syntax_run.py"
        assert not bad_path.exists(), (
            "case (e) failed: bad_syntax_run.py was written despite "
            "SyntaxError"
        )
        assert "# !err: SyntaxError" in result, (
            "case (e) failed: missing `# !err: SyntaxError` annotation"
        )
        assert "# val: yes" in result, (
            "case (e) failed: notebook didn't recover after SyntaxError block"
        )

        # (f) comma form: file written, body ran
        comma_path = files_dir / "comma_form_run.py"
        assert comma_path.is_file(), (
            "case (f) failed: comma form did not write comma_form_run.py"
        )
        assert "# out: comma form ran" in result, (
            "case (f) failed: comma form body did not execute"
        )

        # (g) inner `# in:` feeds subprocess stdin; outer `# in:` does NOT leak
        stdin_path = files_dir / "stdin_iso.py"
        assert stdin_path.is_file(), "case (g) failed: stdin_iso.py missing"
        assert "# out: got: 42" in result, (
            "case (g) failed: inner `# in: 42` didn't reach input()"
        )
        assert "# out: got: 999" not in result, (
            "case (g) failed: outer `# in: 999` leaked into subprocess"
        )

        print("\n✅ all save-and-RUN smoke-test cases passed")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
