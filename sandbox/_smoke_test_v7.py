"""Smoke tests for v7 features."""
import sys, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from inline_output_v7 import run_and_annotate, _strip_old_annotations  # noqa


def _run(src: str, fname: str = "_v7smoke.py") -> str:
    target_dir = HERE / "_v7smoke_dir"
    target_dir.mkdir(exist_ok=True)
    files_dir = target_dir / "files"
    files_dir.mkdir(exist_ok=True)
    target = target_dir / fname
    target.write_text(src)
    run_and_annotate(str(target), files_dir=files_dir)
    return target.read_text()


def case(name, src, expectations):
    out = _run(src)
    failed = []
    for needle in expectations:
        if needle not in out:
            failed.append(needle)
    status = "PASS" if not failed else "FAIL"
    print(f"[{status}] {name}")
    if failed:
        print("  missing:")
        for f in failed:
            print(f"    {f!r}")
        print("  --- output ---")
        print(out)
        print("  --------------")
    return not failed


results = []

# 1. Auto-show under `with Scratch as a:`
results.append(case(
    "auto-show with Scratch as a:",
    'with Scratch as a:\n    print("hi")\n    print("bye")\n',
    ["# a.out: hi", "# a.out: bye"],
))

# 2. New short shape `with "FILE.py" as a:` (save+run+capture+auto-show)
results.append(case(
    "with \"FILE.py\" as a:",
    'with "_v7_a.py" as a:\n    print("from a")\n',
    ["# a.out: from a"],
))

# 3. Crash isolation under `with Scratch:` (no capture)
results.append(case(
    "crash isolation no-capture",
    'with Scratch:\n    1/0\nprint("after")\n',
    ["# !err: ZeroDivisionError",
     "# out: after"],
))

# 4. Crash isolation under capture form, traceback shows user line
results.append(case(
    "crash isolation with capture + line ref",
    'with Scratch as a:\n    raise ValueError("oops")\nprint("kept going")\n',
    ["# !err: ValueError: oops",
     "at line 2",
     "# out: kept going"],
))

# 5. Sandbox alias for RUN
results.append(case(
    "Sandbox alias",
    'with Sandbox:\n    print("sb")\n',
    ["# out: sb"],
))

# 6. Plain Scratch with `as` but normal name (not reserved)
results.append(case(
    "Scratch with capture name = 'p1'",
    'with Scratch as p1:\n    print("one")\n',
    ["# p1.out: one"],
))

# 7. Idempotency: re-running must not duplicate `# <name>.out:` lines.
def _idempotency():
    src = 'with Scratch as a:\n    print("x")\n'
    out1 = _run(src, fname="_v7_idem.py")
    target = HERE / "_v7smoke_dir" / "_v7_idem.py"
    run_and_annotate(str(target), files_dir=HERE / "_v7smoke_dir" / "files")
    out2 = target.read_text()
    n1 = out1.count("# a.out: x")
    n2 = out2.count("# a.out: x")
    ok = n1 == 1 and n2 == 1
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] idempotency: 1st run={n1}, 2nd run={n2}")
    if not ok:
        print(out2)
    return ok


results.append(_idempotency())

print()
print(f"{sum(results)}/{len(results)} v7 cases pass")

# cleanup
shutil.rmtree(HERE / "_v7smoke_dir", ignore_errors=True)
sys.exit(0 if all(results) else 1)
