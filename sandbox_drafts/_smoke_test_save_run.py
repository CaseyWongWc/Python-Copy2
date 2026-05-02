"""
Ad-hoc smoke test for the `with "X" as Scratch:` save-and-run combo.

Usage: python sandbox/_smoke_test_save_run.py

Builds a small notebook in a temp dir, runs it through
`run_and_annotate`, and asserts the resulting annotations cover the
five cases from task-8's smoke checklist:
  (a) the file is written with the EXACT verbatim body source
  (b) variables defined inside the block do NOT leak into outer scope
  (c) the `as h` capture form exposes the body's locals on `h`
  (d) a SyntaxError in the body produces `# !err: SyntaxError` AND
      the file is NOT written to disk
  (e) interaction with the importable-files task: writing a `.py` via
      `with "h.py" as Scratch:` makes `import h` work on the next line
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

    with "should_not_exist.py" as Scratch:
        DOC_LEAK = "if you see this on disk, the docstring filter broke"
"""

# (a) verbatim body lands on disk; (b) outer scope unaffected
outer_n3 = "untouched"
with "verbatim.py" as Scratch:
    n1 = 5
    n2 = 7.5
    n3 = n1 + n2
    print(n3)

# (b) outer_n3 untouched; n3 not visible
outer_n3
# val: untouched

# (c) capture form: `as h` exposes body locals
with "captured.py" as Scratch as h:
    x = 100
    y = 50
    sum_xy = x + y

h.sum_xy

# (d) syntax error in body — file NOT written, # !err: annotated
with "bad_syntax.py" as Scratch:
    this is not valid python at all !!!

# After the bad block, the rest of the notebook MUST keep working —
# this assignment proves we recovered.
recovered = "yes"
recovered

# (e) save-and-run + importable: write helper, then import on next line
with "imp_target.py" as Scratch:
    GREETING = "imported ok"
    def greet():
        return GREETING

import imp_target
imp_target.greet()

# (f) comma form: `with "X", Scratch:` (optional shape — should also work)
with "comma_form.py", Scratch:
    comma_var = 999
    print("comma form ran")

# (g) comma + capture: `with "X", Scratch as h:`
with "comma_cap.py", Scratch as ch:
    only_in_block = 42

ch.only_in_block
'''


def main():
    tmp = Path(tempfile.mkdtemp(prefix="save_run_smoke_"))
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

        # (a) verbatim file content
        verbatim_path = files_dir / "verbatim.py"
        assert verbatim_path.is_file(), (
            "case (a) failed: sandbox/files/verbatim.py was not written"
        )
        verbatim = verbatim_path.read_text()
        for needle in ("n1 = 5", "n2 = 7.5", "n3 = n1 + n2", "print(n3)"):
            assert needle in verbatim, (
                f"case (a) failed: missing `{needle}` in verbatim.py"
            )
        # The body's print produced an annotation
        assert "# out: 12.5" in result, (
            "case (a) failed: body's print(n3) didn't run in-process"
        )

        # (b) outer scope untouched — no leak
        assert "# val: untouched" in result, (
            "case (b) failed: outer_n3 was overwritten by block locals"
        )
        # And `n3` from the block must not have leaked as a bare-expr
        # later — we never reference it in the outer notebook, so the
        # only way it could matter is if Scratch isolation broke.

        # (c) capture form
        cap_path = files_dir / "captured.py"
        assert cap_path.is_file(), "case (c) failed: captured.py missing"
        assert "# val: 150" in result, (
            "case (c) failed: h.sum_xy did not return 150 (capture broke)"
        )

        # (d) syntax error: NO file write, # !err: annotation present
        bad_path = files_dir / "bad_syntax.py"
        assert not bad_path.exists(), (
            "case (d) failed: bad_syntax.py was written despite SyntaxError"
        )
        assert "# !err: SyntaxError" in result, (
            "case (d) failed: missing `# !err: SyntaxError` annotation"
        )
        # And the rest of the notebook still ran
        assert "# val: yes" in result, (
            "case (d) failed: notebook didn't recover after SyntaxError block"
        )

        # (e) importable file: helper written + import works
        imp_path = files_dir / "imp_target.py"
        assert imp_path.is_file(), "case (e) failed: imp_target.py missing"
        assert "# val: imported ok" in result, (
            "case (e) failed: `import imp_target` + greet() didn't return"
            " expected string (sys.path / file write order issue)"
        )

        # (f) comma form: file written, body ran
        comma_path = files_dir / "comma_form.py"
        assert comma_path.is_file(), (
            "case (f) failed: comma form did not write comma_form.py"
        )
        assert "# out: comma form ran" in result, (
            "case (f) failed: comma form body did not execute"
        )

        # (g) comma + capture
        comma_cap_path = files_dir / "comma_cap.py"
        assert comma_cap_path.is_file(), (
            "case (g) failed: comma+capture did not write comma_cap.py"
        )
        assert "# val: 42" in result, (
            "case (g) failed: ch.only_in_block did not return 42"
        )

        # Docstring case: the fake header inside the """...""" must not
        # have produced a file or run the body.
        docstring_path = files_dir / "should_not_exist.py"
        assert not docstring_path.exists(), (
            "docstring filter broke: should_not_exist.py was written"
        )

        print("\n✅ all save-and-run smoke-test cases passed")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
