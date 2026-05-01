from inline_output_v5 import run_and_annotate

TARGET = "zypaste.py"  # file you're working in
APPEND_TO = "zy_log.py"  # your growing notebook log
CLEAR_TARGET = False  # flip to True when done with a problem
CLEAR_HEADER = "from Helpers.helpings import *"

run_and_annotate(
    "goog.py", append_to="zy_log.py", clear_target=False, clear_header=CLEAR_HEADER
)
