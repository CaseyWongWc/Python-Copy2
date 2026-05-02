"""
Ad-hoc smoke test for the `with RUN:` block.

Usage: python sandbox/_smoke_test_run.py

Builds a small notebook in a temp dir, runs it through
`run_and_annotate`, and asserts the resulting annotations cover the
six cases from task-7's smoke checklist:
  (a) successful run with stdout    — print result lands as `# out:`
  (b) NameError when an outer var   — `# err:` traceback + `# !err:`
  (c) `with RUN: -V`                 — Python version string in `# out:`
  (d) `with RUN:` inside a docstring — left alone (no annotations)
  (e) `import main` inside RUN works (sandbox/files on PYTHONPATH)
  (f) `# in:` inside RUN body feeds the subprocess's stdin (and the
      OUTER `# in:` queue is NOT shared with the subprocess)
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

    with RUN:
        print("docstring contents — must not run")
"""

# (a) successful stdout
with RUN:
    x = 5
    y = 7
    print(x + y)

# (b) NameError when referencing an outer variable
outer = "I am outside"
with RUN:
    print(outer)

# (c) -V flag returns Python version string
with RUN: -V
    pass

# (e) `import main` works — sandbox/files/main.py is on PYTHONPATH
with "main.py":
    GREETING = "hi from main"

# An OUTER `# in:` queue value that the subprocess must NOT see —
# if isolation leaks, `prove_isolation` below would consume "999".
# in: 999
with RUN:
    import main
    print(main.GREETING)

# (f) `# in:` inside a RUN body feeds that subprocess's stdin only
with RUN:
    # in: 42
    n = int(input())
    print("got:", n)
'''


def main():
    tmp = Path(tempfile.mkdtemp(prefix="run_smoke_"))
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

        # (a) print(x + y) -> # out: 12
        assert "# out: 12" in result, "case (a) failed: missing `# out: 12`"

        # (b) NameError on `outer`
        assert "NameError" in result and "outer" in result, (
            "case (b) failed: expected NameError on `outer`"
        )
        assert "# !err: subprocess exited with code" in result, (
            "case (b) failed: expected non-zero exit annotation"
        )

        # (c) -V returns "Python 3.x.y"
        assert "# out: Python 3" in result or "# err: Python 3" in result, (
            "case (c) failed: expected Python version string in -V output"
        )

        # (d) docstring contents must not be annotated
        # The docstring's `print("docstring contents...")` should NOT have
        # produced an annotation.
        assert "docstring contents — must not run" not in result.split(
            '"""', 2
        )[2], "case (d) failed: docstring body was processed"
        # Same for any `# out:` referencing it
        assert "# out: docstring contents" not in result, (
            "case (d) failed: docstring `with RUN:` was executed"
        )

        # (e) `import main` works inside a RUN block
        assert "# out: hi from main" in result, (
            "case (e) failed: `import main` inside RUN didn't print "
            "expected greeting (PYTHONPATH likely missing files_dir)"
        )

        # (f) `# in:` inside RUN body feeds stdin
        assert "# out: got: 42" in result, (
            "case (f) failed: `# in:` inside RUN body didn't reach input()"
        )
        # And the OUTER `# in: 999` must NOT have been consumed by the
        # subprocess — it would have replaced "42" if isolation leaked.
        assert "# out: got: 999" not in result, (
            "case (f) failed: outer `# in:` queue leaked into subprocess"
        )

        # And the .run_blocks dir should exist (was auto-created)
        assert (files_dir / ".run_blocks").is_dir(), (
            "missing .run_blocks/ scratch dir"
        )

        print("\n✅ all 6 smoke-test cases passed")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
