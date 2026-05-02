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


# --- 5a. Sibling packages next to goog.py are also importable ---------------
# Drop a folder like `Helpers/` (with `helpings.py` inside) right next to
# `goog.py` in `sandbox/notebook/`, and any import works the same way it
# did at the project root. `with RUN:` subprocesses inherit this too via
# PYTHONPATH, so imports work in fresh-process mode as well.
#
#   from Helpers.helpings import *
#   INFO()


# --- 5b. `with "X" as Scratch:` — save AND run in one block -----------------
# Combines `with "X":` (write file) + `with Scratch:` (run isolated). The
# body lands on disk verbatim AND runs in-process; vars defined inside
# don't leak. Use this when you want a helper file written AND its setup
# logic executed in the same step.
#
# Before (two steps — file write, then a separate Scratch run):
#   with "tally.py":
#       a = 5
#       b = 7.5
#       total = a + b
#   with Scratch:
#       a = 5             # had to retype the body to actually run it
#       b = 7.5
#       total = a + b
#       print(total)
#
# After (one step):
with "tally.py" as Scratch:
    a = 5
    b = 7.5
    total = a + b
    print(total)
# Outer scope can't see a/b/total — Scratch isolation. But
# sandbox/files/tally.py exists too, ready for `import tally` later.

# Capture form: `as h` exposes the body's locals on `h`, just like plain
# `with Scratch as h:`. Comma form (`with "X", Scratch:` / `with "X",
# Scratch as h:`) also works if you prefer Python's native multi-context
# syntax.
with "tally2.py" as Scratch as h:
    x = 100
    y = 50
    sum_xy = x + y

h.sum_xy
# val: 150


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


# --- 7b. `with "X" as RUN:` — save AND run in fresh subprocess --------------
# Combines `with "X":` (write file) + `with RUN:` (fresh-subprocess run)
# into one block. The body lands on disk verbatim AT the resolved path
# AND runs in a brand-new `python3` subprocess. Use this when you want
# a script saved AND executed with full process isolation (no leftover
# globals, no cached imports). Stronger isolation than `with "X" as
# Scratch:` (that one just isolates the namespace inside the same
# Python process). All `with RUN:` rules carry over: stdout/stderr land
# under the LAST non-blank body line, non-zero exit appends `# !err:
# subprocess exited with code N`, inline argv (`with "X" as RUN: -O`)
# works, body's `# in:` directives feed the subprocess's stdin, and
# the outer notebook's `# in:` queue is NOT shared.
#
# Before (two steps — write file, then run with subprocess):
#   with "demo.py":
#       a = 5
#       b = 7
#       print(a + b)
#   with RUN:
#       a = 5             # had to retype the body to actually run it
#       b = 7
#       print(a + b)
#
# After (one step):
with "demo.py" as RUN:
    a = 5
    b = 7
    print(a + b)
# sandbox/files/demo.py exists too, ready to be re-run later.

# Inline argv works just like plain RUN.
with "vflag.py" as RUN: -V
    pass

# Comma form `with "X", RUN:` is also accepted.
with "comma.py", RUN:
    print("comma form ran")

# Body is invalid Python -> `# !err: SyntaxError` on the header line
# AND the file is NOT written (mirrors `with "X" as Scratch:`).


# --- 8. Magic save still works ----------------------------------------------
# Add a `# zy: 12.1 MyExample` (or `# quick:`, `# note:`, `# save:`) at the
# top of this file to auto-save a copy after annotation.


# --- 9. Indentation help (phone-typing friendly) ----------------------------
# The runner quietly fixes the most common phone-keyboard whitespace slips
# BEFORE parsing your file:
#   - leading TAB characters become 4 spaces
#   - leading non-breaking spaces (the invisible U+00A0 some keyboards
#     insert) become regular spaces
# Only the LEADING whitespace of each line is touched, so a tab inside a
# string (`print("a\tb")` or inside a triple-quoted string) is preserved.
#
# When indentation IS broken in a way the auto-fix can't resolve, you get
# a friendly multi-line error instead of a raw Python traceback:
#
#   def foo():
#       x = 1
#      y = 2          # ← only 3 spaces, mismatched
#   # !err: --- ERROR ---
#   # !err: IndentationError on line 3: indented 3 space(s), but no
#   #       open block matches that level.
#   # !err:   line 2 was indented 4 space(s) — pick a level that lines
#   #       up with an outer block.
#
# Same for missing indent after a `:` ("this line needs to be indented")
# and plain SyntaxError ("SyntaxError on line N: ..." instead of a
# 5-line traceback).
