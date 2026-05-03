# ===================================================================
# goog_cheatsheet.py — one-screen tour of every magic `with` block
# ===================================================================
# Click Run. Each section below is independent, so you can scroll
# through and see exactly what each pattern does. Annotations get
# regenerated on every run, so don't worry about messing them up.
# Copy-paste any block you like into your real goog.py.
# ===================================================================


# ---  1) with "filename":  ----------------------------------------
# Writes the indented body AS RAW TEXT to the file. The body is
# never parsed as Python, so it can be ANY text (markdown, csv, json,
# python source, whatever). Bare names land in sandbox/files/.
with "hello.txt":
    Hello, world!
    This is just text — no Python rules apply.


# ---  2) with Scratch:  -------------------------------------------
# Runs the body, but variables defined inside DON'T leak out.
# Great for trying something without polluting your namespace.
# (with _:  and  with __:  do the same thing.)
x = "outer"

with Scratch:
    x = "inner — only visible inside this block"
    x          # # val: ...

x              # # val: outer   ← outer x untouched


# ---  3) with Scratch as a:  --------------------------------------
# Same as above, but afterward `a.<name>` gives you the locals
# the block defined. Lets you grab things back without polluting
# the outer scope by accident.
with Scratch as a:
    name = "Casey"
    score = 42

a.name         # # val: Casey
a.score        # # val: 42


# ---  4) # in: <value>  -------------------------------------------
# Queues a value to be fed to the next input() call. Use one
# `# in:` per input(), in order. Saves you from typing while testing.
# in: Alice
# in: 99
who   = input("name?  ")
score = int(input("score? "))
print(who, score)             # # out: Alice 99


# ---  5) with bash:  ----------------------------------------------
# Run shell commands. Each line is its own command. stdout shows
# as `# out:`, stderr as `# err:`, non-zero exit as `# !err:`.
# Runs from sandbox/files/, NOT the notebook folder.
with bash:
    echo "hi from the shell"
    pwd
    ls | head -3


# ---  6) with RUN:  -----------------------------------------------
# Runs the body in a FRESH python3 subprocess (totally isolated —
# no shared variables, no shared imports). Useful if you want to
# test something cleanly or if your code has a `sys.exit()`.
with RUN:
    print("I am a clean python process")
    import sys
    print("python:", sys.version_info[:2])


# ---  7) with "X" as Scratch:  ------------------------------------
# Save body to file X *and* run it sandboxed (locals don't leak).
# Combo of pattern 1 + pattern 2. Two-for-one.
with "demo_scratch.py" as Scratch:
    msg = "saved AND run sandboxed"
    print(msg)


# ---  8) with "X" as RUN:  ----------------------------------------
# Save body to file X *and* run it as a fresh subprocess.
# If it errors, the traceback points at the saved file (so you
# can open it and fix it). Combo of pattern 1 + pattern 6.
with "demo_run.py" as RUN:
    print("saved AND run as a subprocess")
    for i in range(3):
        print("tick", i)


# ===================================================================
# Tips:
#   - `# out: text`  prints from your code   ← runner adds these
#   - `# val: 42`    expression value         ← runner adds these
#   - `# !err: ...`  errors / tracebacks      ← runner adds these
#   - `# in:  hi`    YOU type these to feed input()
# ===================================================================
