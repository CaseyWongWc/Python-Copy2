# Sandbox notebook — v6 cheat sheet
#
# Click Run (or run sandbox/notebook/main.py) and this whole file is
# annotated inline:
#   print()         -> # out:
#   bare exprs      -> # val:
#   tracebacks      -> # !err:
#
# The four magic moves on top of v4:
#
#   with "name.txt":         -> writes the indented block (raw text) to a file
#   with Scratch:            -> runs the block but vars don't leak out
#   with Scratch as a:       -> same, but captures vars onto `a`
#   # in: <value>            -> queues a value for the next input() call
#
# Bare names like "name.txt" land in sandbox/files/.
# Paths with a slash are relative to sandbox/notebook/.
# Absolute paths go exactly where you write them.


# --- 1. Inline file creation -------------------------------------------------

with "names.txt":
    Tia
    Lynn
    Ravi

contents = open("../files/names.txt").read()
contents


# --- 2. Sandbox scope (vars don't leak) --------------------------------------

x = 100
with Scratch:
    x = 5            # local to the block
    helper = "temp"  # also local to the block

x                   # still 100 — Scratch reverted it


# --- 3. Sandbox scope with capture ------------------------------------------

with Scratch as a:
    name = "Casey"
    score = 42

a.name
a.score


# --- 4. Comment-driven inputs -----------------------------------------------

# in: 7
# in: 3
n = int(input("first: "))
m = int(input("second: "))
n + m


# --- 5. Magic save still works ----------------------------------------------
# Add a `# zy: 12.1 MyExample` (or `# quick:`, `# note:`, `# save:`) at the
# top of this file to auto-save a copy after annotation.
# !err: --- ERROR ---
# !err: Traceback (most recent call last):
# !err:   File "<string>", line 63, in <module>
# !err:   File "goog.py", line 23, in <module>
# !err:     with "names.txt":
# !err: TypeError: 'str' object does not support the context manager protocol
