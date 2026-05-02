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
# Path rules (kept simple on purpose):
#   "name.txt"        -> sandbox/files/name.txt
#   "sub/name.txt"    -> sandbox/files/sub/name.txt
#   "/abs/path.txt"   -> exactly that absolute path
#
# `open("name.txt")` reads from the SAME place `with "name.txt":` writes
# to, because the runner cd's into sandbox/files/ before running you.


# --- 1. Inline file creation -------------------------------------------------

with "names.txt":
    Tia
    Lynn
    Ravi

contents = open("names.txt").read()
contents
# val: Tia
# val: Lynn
# val: Ravi


# --- 2. Sandbox scope (vars don't leak) --------------------------------------

x = 100
with Scratch:
    x = 5            # local to the block
    helper = "temp"  # also local to the block

x                   # still 100 — Scratch reverted it
# val: 100


# --- 3. Sandbox scope with capture ------------------------------------------

with Scratch as a:
    name = "Casey"
    score = 42

a.name
# val: Casey
a.score
# val: 42


# --- 4. Comment-driven inputs -----------------------------------------------

# in: 7
# in: 3
n = int(input("first: "))
# out: first: 7
m = int(input("second: "))
# out: second: 3
n + m
# val: 10


# --- 5. Write a helper, then import it --------------------------------------
# `with "helper.py":` writes to sandbox/files/helper.py, and that folder is
# on sys.path inside the notebook run, so `import helper` Just Works.
# `with "subdir/helper.py":` also works — empty __init__.py files are
# auto-created so `from subdir import helper` resolves.

with "greet_helper.py":
    def greet(name):
        return f"hi, {name}!"

import greet_helper
greet_helper.greet("Casey")
# val: hi, Casey!


# --- 6. Shell commands inline -----------------------------------------------
# `with bash:` runs each indented body line through `/bin/sh -c`, with cwd
# at sandbox/files/. After the run:
#   stdout       -> # out:
#   stderr       -> # err:    (lowercase, distinct from # !err:)
#   non-zero rc  -> # !err: exit code N
# Each line is one independent command. Comments and blank lines in the
# body are preserved and ignored. A failing command does NOT stop the
# rest of the notebook.

with bash:
    cat names.txt
    cat does-not-exist


# --- 7. Fresh-subprocess `with RUN:` ----------------------------------------
# `with RUN:` writes the indented body to a temp file under
# `sandbox/files/.run_blocks/` and runs it in a brand-new `python3`
# subprocess. Globals from the surrounding notebook are NOT visible
# inside (true process isolation, stronger than `Scratch`'s namespace
# isolation). Stdout becomes `# out:` lines, stderr becomes `# err:`,
# and a non-zero exit appends `# !err: subprocess exited with code N`.
# Pass extra python3 args inline: `with RUN: -O`, `with RUN: -V`, etc.

# (a) Plain run — stdout flows back as `# out:`
with RUN:
    x = 5
    y = 7
    print(x + y)

# (b) `outside_var` is invisible to the subprocess — fresh interpreter
outside_var = "you can't see me"
with RUN:
    print(outside_var)   # NameError, by design

# (c) Pass args to python3 — `-V` prints the version on stderr/stdout
with RUN: -V
    pass


# --- 8. Magic save still works ----------------------------------------------
# Add a `# zy: 12.1 MyExample` (or `# quick:`, `# note:`, `# save:`) at the
# top of this file to auto-save a copy after annotation.
