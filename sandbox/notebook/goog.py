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
    # val: inner — only visible inside this block

x              # # val: outer   ← outer x untouched
# val: outer


# ---  3) with Scratch as a:  --------------------------------------
# Same as above, but afterward `a.<name>` gives you the locals
# the block defined. Lets you grab things back without polluting
# the outer scope by accident.
with Scratch as a:
    name = "Casey"
    score = 42

a.name         # # val: Casey
# val: Casey
a.score        # # val: 42
# val: 42


# ---  4) # in: <value>  -------------------------------------------
# Queues a value to be fed to the next input() call. Use one
# `# in:` per input(), in order. Saves you from typing while testing.
# in: Alice
# in: 99
who   = input("name?  ")
# out: name?  Alice
score = int(input("score? "))
# out: score? 99
print(who, score)             # # out: Alice 99
# out: Alice 99


# ---  5) with bash:  ----------------------------------------------
# Run shell commands. Each line is its own command. stdout shows
# as `# out:`, stderr as `# err:`, non-zero exit as `# !err:`.
# Runs from sandbox/files/, NOT the notebook folder.
with bash:
    echo "hi from the shell"
    # out: hi from the shell
    pwd
    # out: /home/runner/workspace/sandbox/files
    ls | head -3
    # out: a.py
    # out: asdfasdlfjkdhasdlkfasdf.py
    # out: b.py


# ---  6) with RUN:  -----------------------------------------------
# Runs the body in a FRESH python3 subprocess (totally isolated —
# no shared variables, no shared imports). Useful if you want to
# test something cleanly or if your code has a `sys.exit()`.
with RUN:
    print("I am a clean python process")
    import sys
    print("python:", sys.version_info[:2])
    # out: I am a clean python process
    # out: python: (3, 11)


# ---  7) with "X" as Scratch:  ------------------------------------
# Save body to file X *and* run it sandboxed (locals don't leak).
# Combo of pattern 1 + pattern 2. Two-for-one.
with "demo_scratch.py" as Scratch:
    msg = "saved AND run sandboxed"
    print(msg)
    # out: saved AND run sandboxed


# ---  8) with "X" as RUN:  ----------------------------------------
# Save body to file X *and* run it as a fresh subprocess.
# If it errors, the traceback points at the saved file (so you
# can open it and fix it). Combo of pattern 1 + pattern 6.
with "demo_run.py" as RUN:
    print("saved AND run as a subprocess")
    for i in range(3):
        print("tick", i)
        # out: saved AND run as a subprocess
        # out: tick 0
        # out: tick 1
        # out: tick 2


# ===================================================================
# Tips:
#   - `# out: text`  prints from your code   ← runner adds these
#   - `# val: 42`    expression value         ← runner adds these
#   - `# !err: ...`  errors / tracebacks      ← runner adds these
#   - `# in:  hi`    YOU type these to feed input()
# ===================================================================
##############################################################################
# in: 99

with "z.py" as a:
    v = input()
    # out: 99
    print(v)
    # out: 99
    # a.out: 99
1
# val: 1
# in: 1
with bash:
    echo "hi"
    # out: hi
    3
    # err: /bin/sh: 1: 3: not found
    # !err: exit code 127
    python z.py <<< "99"
    # err: /bin/sh: 1: Syntax error: redirection unexpected
    # !err: exit code 2
    9
    # err: /bin/sh: 1: 9: not found
    # !err: exit code 127
2
# val: 2
# in: 1
with "z.py" as RUN:
    v = input()
    print(v)
    # err: Traceback (most recent call last):
    # err:   File "/home/runner/workspace/sandbox/files/z.py", line 1, in <module>
    # err:     v = input()
    # err:         ^^^^^^^
    # err: EOFError: EOF when reading a line
    # !err: subprocess exited with code 1
with "z.py":
    print("hello")
    abc=1
    v = input()
    print(v)
with bash:
    cat z.py
    # out: v = input()
    # out: print(v)
with "z.py" as _:
    v = input()
    # out: 1
    print(v)
    # out: 1
    a = 123
    a
    # val: 123
    

with bash:
    cat z.py
    # out: v = input()
    # out: print(v)
with "asdfasdlfjkdhasdlkfasdf.py" as _:
    v = input()
    # out: 1
    print(v,12345)
    # out: 1 12345
with "hey.py":
    print("hey")
with bash:
    cat hey.py
    # out: print("hey")
    python hey.py
    # out: hey
with "hey2.py":
    i=input()
    print("hey")
# in: 1
with bash:
    cat hey2.py
    # out: h=input()
    # out: print("hey")
    python hey2.py
    # err: Traceback (most recent call last):
    # err:   File "/home/runner/workspace/sandbox/files/hey2.py", line 1, in <module>
    # err:     h=input()
    # err:       ^^^^^^^
    # err: EOFError: EOF when reading a line
    # !err: exit code 1
    2
    # err: /bin/sh: 1: 2: not found
    # !err: exit code 127
# in: 1
with "hey2.py" as RUN:
    h=input()
    print("hey")
    # err: Traceback (most recent call last):
    # err:   File "/home/runner/workspace/sandbox/files/hey2.py", line 1, in <module>
    # err:     h=input()
    # err:       ^^^^^^^
    # err: EOFError: EOF when reading a line
    # !err: subprocess exited with code 1
with "hey2.py" as RUN:
    # in: 1
    h=input()
    print("hey")
    # out: hey

# in: 30jkjk
with r"hey2.py" as Scratch:
    h=input()
    # out: 1
    print("hey")
    # out: hey
# in: 676767
with r"hey4.py" as b:
    m=input()
    # out: 676767
    print("hey")
    # out: hey
    # b.out: hey
# in: 67
with bash:
    python hey4.py
    # err: Traceback (most recent call last):
    # err:   File "/home/runner/workspace/sandbox/files/hey4.py", line 1, in <module>
    # err:     m=input()
    # err:       ^^^^^^^
    # err: EOFError: EOF when reading a line
    # !err: exit code 1
# in: 67
# in: abc
with r"z123.py" as Scratch2:
     v = input()
     # out: 67
     print(v)
     # out: 67
     # Scratch2.out: 67
3
# val: 3
# in: g
with "a.py"  as Scratch:
    print("hello")
    # out: hello
    input()
    # out: g
    # val: g

with "b.py":
    hey=input()
with bash:
    python3 "b.py" >>> "123"
    # err: /bin/sh: 1: Syntax error: redirection unexpected
    # !err: exit code 2
    1
    # err: /bin/sh: 1: 1: not found
    # !err: exit code 127
    python3 b.py <<< "123"
    # err: /bin/sh: 1: Syntax error: redirection unexpected
    # !err: exit code 2
with "b.py" as Scratch:
    hey=input()
    # err: Traceback (most recent call last):
    # err:   File "/home/runner/workspace/sandbox/files/b.py", line 1, in <module>
    # err:     hey=input()
    # err:         ^^^^^^^
    # err: EOFError: EOF when reading a line
    # !err: subprocess exited with code 1
with "b.py" as RUN:
    hey=input()
