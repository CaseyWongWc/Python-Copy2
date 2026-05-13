from inline_output_v5 import run_and_annotate

TARGET = "goog.py"  # file you are actively working in
LOG = "zy_log.py"  # cumulative ZyBooks notebook (only grows, never wiped)

# ── change these two to whatever symbols you like ────────────────────────────
SECTION_MARKER = ";"  # wrap a finished block top + bottom  →  logged & deleted
CLEAR_MARKER = "⭐"  # put anywhere on its own line         →  whole file logged & wiped
# ─────────────────────────────────────────────────────────────────────────────

result = run_and_annotate(
    path=TARGET,
    append_to=LOG,
    section_marker=SECTION_MARKER,
    clear_marker=CLEAR_MARKER,
)

print(result)
