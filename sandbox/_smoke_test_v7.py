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


# 8. Stale `# in:` from earlier in source gets shadowed by a fresh
#    `# in:` typed right before the next block (Casey's "got 1 instead
#    of 676767" footgun).
def _stale_input_shadowed():
    src = (
        '# in: 1\n'
        'noop = "between blocks"\n'
        '# in: 676767\n'
        'with Scratch:\n'
        '    v = input()\n'
        '    print(v)\n'
    )
    out = _run(src, fname="_v7_stale.py")
    ok = "# out: 676767" in out and "# out: 1\n" not in out
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] stale `# in:` shadowed by newer batch")
    if not ok:
        print(out)
    return ok


# 9. Multi-input batch (3 # in: in a row, 3 input() calls): all values
#    feed in order — batch-shadowing must NOT eat them.
def _multi_input_batch():
    src = (
        '# in: a\n'
        '# in: b\n'
        '# in: c\n'
        'with Scratch:\n'
        '    print(input())\n'
        '    print(input())\n'
        '    print(input())\n'
    )
    out = _run(src, fname="_v7_multi.py")
    # Each input() echoes value via mock_input AND print() prints it,
    # so each appears 2x. We just need a, b, c to all show up in order.
    pa, pb, pc = out.find("# out: a"), out.find("# out: b"), out.find("# out: c")
    ok = 0 <= pa < pb < pc
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] multi-input batch (3 in a row)")
    if not ok:
        print(out)
    return ok


# 10. Legacy `# RUN out:` lines get stripped before saving to disk
#     (so they can't leak into `with "FILE.py" as RUN:` files).
def _run_prefix_stripped():
    target_dir = HERE / "_v7smoke_dir"
    target_dir.mkdir(exist_ok=True)
    files_dir = target_dir / "files"
    files_dir.mkdir(exist_ok=True)
    target = target_dir / "_v7_runstrip.py"
    target.write_text(
        'with "stripme.py" as RUN:\n'
        '    print("hi")\n'
        '    # RUN out: hi\n'
    )
    run_and_annotate(str(target), files_dir=files_dir)
    saved = (files_dir / "stripme.py").read_text()
    ok = "RUN out:" not in saved and 'print("hi")' in saved
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] `# RUN out:` stripped from saved file")
    if not ok:
        print("--- saved ---")
        print(saved)
    return ok


results.append(_stale_input_shadowed())
results.append(_multi_input_batch())
results.append(_run_prefix_stripped())


# 11. `with r"FILE.py":` (terse subprocess) — non-empty body saves
#     the file then runs it; output appears as `# out:` below body.
def _raw_str_with_body():
    target_dir = HERE / "_v7smoke_dir"
    target_dir.mkdir(exist_ok=True)
    files_dir = target_dir / "files"
    files_dir.mkdir(exist_ok=True)
    target = target_dir / "_v7_raw_body.py"
    target.write_text(
        'with r"_v7_rawbody.py":\n'
        '    print("hello from raw")\n'
    )
    run_and_annotate(str(target), files_dir=files_dir)
    out = target.read_text()
    saved = (files_dir / "_v7_rawbody.py").read_text()
    ok = "# out: hello from raw" in out and 'print("hello from raw")' in saved
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] `with r\"FILE.py\":` saves body and runs subprocess")
    if not ok:
        print(out)
    return ok


# 12. `with r"FILE.py":` body lands in fresh subprocess (proves
#     process isolation, not in-process Scratch behavior).
def _raw_str_subprocess_isolated():
    target_dir = HERE / "_v7smoke_dir"
    target_dir.mkdir(exist_ok=True)
    files_dir = target_dir / "files"
    files_dir.mkdir(exist_ok=True)
    target = target_dir / "_v7_raw_iso.py"
    # `__name__ == "__main__"` only prints when the file is run as a
    # script, which proves it ran in a subprocess (not just imported
    # or evaluated in-process by Scratch).
    target.write_text(
        'with r"_v7_iso.py":\n'
        '    if __name__ == "__main__":\n'
        '        print("ran as script")\n'
    )
    run_and_annotate(str(target), files_dir=files_dir)
    out = target.read_text()
    ok = "# out: ran as script" in out
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] `with r\"FILE.py\":` runs in fresh subprocess")
    if not ok:
        print(out)
    return ok


results.append(_raw_str_with_body())
results.append(_raw_str_subprocess_isolated())

print()
print(f"{sum(results)}/{len(results)} v7 cases pass")

# cleanup
shutil.rmtree(HERE / "_v7smoke_dir", ignore_errors=True)
sys.exit(0 if all(results) else 1)
