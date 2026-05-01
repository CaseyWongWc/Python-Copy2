from inline_output_v4 import run_and_annotate, _strip_old_annotations
from pathlib import Path

TARGET = "goog.py"

# ── optional: clean annotations back out of goog.py after saving ─────────────
# goog.py is NEVER emptied — your code always stays there.
# When False (default): annotations stay inlined in goog.py after each run.
# When True:  annotations are stripped back out after the magic-comment save,
#             so goog.py returns to plain code, ready for the next problem.
STRIP_AFTER_SAVE = False
# ─────────────────────────────────────────────────────────────────────────────

result = run_and_annotate(TARGET)
print(result)

if STRIP_AFTER_SAVE:
    p = Path(TARGET)
    p.write_text(_strip_old_annotations(p.read_text()))
