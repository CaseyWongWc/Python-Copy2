from inline_output_v5 import run_and_annotate

TARGET  = "goog.py"       # file you are actively working in
LOG     = "zy_log.py"     # cumulative ZyBooks notebook (only grows, never wiped)

# ── marker tokens — set once, use freely inside TARGET ───────────────────────
#
#   SECTION_MARKER  wraps a finished block (top + bottom):
#       ⭐
#       x = 10
#       x
#       ⭐
#   → block is annotated, saved to LOG, then deleted from TARGET.
#   → You can have as many ⭐…⭐ blocks in one file as you like.
#
#   CLEAR_MARKER    anywhere on its own line:
#       ##
#   → whole file is annotated, saved to LOG, then TARGET is wiped clean.
#
# Change either token to whatever you prefer (e.g. "#done", "🔖", "---").

SECTION_MARKER = "⭐"
CLEAR_MARKER   = "##"

# ─────────────────────────────────────────────────────────────────────────────

result = run_and_annotate(
    path           = TARGET,
    append_to      = LOG,
    section_marker = SECTION_MARKER,
    clear_marker   = CLEAR_MARKER,
)

print(result)
