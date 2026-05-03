"""
Sandbox notebook runner.

Click Run on Replit (or `python sandbox/notebook/main.py` from anywhere).
This will:
  1. cd into sandbox/files/ so plain `open("name.txt")` calls in goog.py
     read from the same folder that `with "name.txt":` writes to.
  2. Run inline_output_v7 against goog.py.

Why the cwd is `sandbox/files/` and not `sandbox/notebook/`:
  - `with "names.txt":`         writes to sandbox/files/names.txt
  - `open("names.txt").read()`  now reads from the same place — no
                                `../files/` prefix needed.
  - Absolute paths still work as absolute (e.g. `with "/tmp/x":`).
  - The notebook source file (goog.py) is read by absolute path, so
    chdir doesn't break that.
"""
from Helpers.helpings import *
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SANDBOX_ROOT = HERE.parent
FILES_DIR = SANDBOX_ROOT / "files"

# So `import inline_output_v7` finds the module at <sandbox>/inline_output_v7.py
sys.path.insert(0, str(SANDBOX_ROOT))

# Make sure files/ exists, then cd into it so plain `open("foo.txt")` calls in
# goog.py read from the same folder that `with "foo.txt":` writes to.
FILES_DIR.mkdir(parents=True, exist_ok=True)
os.chdir(FILES_DIR)

from inline_output_v7 import run_and_annotate, _strip_old_annotations  # noqa: E402

# Absolute path because we chdir'd to FILES_DIR, not the notebook dir.
TARGET = str(HERE / "goog.py")

# When True, strip annotations back out of goog.py after the magic-save copy
# (so goog.py returns to plain code). When False (default), annotations stay
# inlined in goog.py.
STRIP_AFTER_SAVE = False

# Mark runner context so goog.py can avoid redirect recursion.
os.environ["GOOG_NOTEBOOK_RUNNER"] = "1"


def run_once() -> str:
    result = run_and_annotate(TARGET)
    print(result)
    if STRIP_AFTER_SAVE:
        p = Path(TARGET)
        p.write_text(_strip_old_annotations(p.read_text()))
    return result


if __name__ == "__main__":
    try:
        run_once()
    except KeyboardInterrupt:
        print("\nStopped.")
