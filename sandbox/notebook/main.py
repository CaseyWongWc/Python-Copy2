"""
Sandbox notebook runner.

Click Run on Replit (or `python sandbox/notebook/main.py` from anywhere).
This will:
  1. cd into sandbox/notebook/ so plain `open("name.txt")` calls in goog.py
     look there.
  2. Run inline_output_v6 against goog.py.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SANDBOX_ROOT = HERE.parent

# So `import inline_output_v6` finds the module at <sandbox>/inline_output_v6.py
sys.path.insert(0, str(SANDBOX_ROOT))

# Run from the notebook dir so `open("foo.txt")` in goog.py looks here.
os.chdir(HERE)

from inline_output_v6 import run_and_annotate, _strip_old_annotations  # noqa: E402

TARGET = "goog.py"

# When True, strip annotations back out of goog.py after the magic-save copy
# (so goog.py returns to plain code). When False (default), annotations stay
# inlined in goog.py.
STRIP_AFTER_SAVE = False


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
