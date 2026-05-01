from inline_output_v5 import run_and_annotate

# ── which file you are actively working in ───────────────────────────────────
TARGET = "goog.py"

# ── cumulative ZyBooks log (grows over time, never overwritten) ───────────────
#    Set to None to skip logging entirely (behaves exactly like v3).
APPEND_TO = "zy_log.py"

# ── set True to wipe TARGET after the run is logged ──────────────────────────
#    Useful when you're done with a problem and want a clean slate.
#    The log already has a timestamped copy, so nothing is lost.
CLEAR_TARGET = False

# ── what stays in TARGET after clearing ──────────────────────────────────────
#    Keeps your standard import so autocomplete still works in the fresh file.
CLEAR_HEADER = "from Helpers.helpings import *"

# ─────────────────────────────────────────────────────────────────────────────

result = run_and_annotate(
    path         = TARGET,
    append_to    = APPEND_TO,
    clear_target = CLEAR_TARGET,
    clear_header = CLEAR_HEADER,
)

print(result)
