from Helpers.helpings import *
from sys import stdout
# out: hello world


def main():
    print("hello world")
    # out: hello world
    print("hello world", file=stdout)
    # out: hello world
    print("hello world", file=stdout, end="")
    # out: hello world
    print("hello world", file=stdout, end="\n")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep="")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world
    print("hello world", file=stdout, end="\n", sep=" ")
    # out: hello world


main()
# val: None


with open("data/module_a.py", "w") as f:
    f.write(r"""def hello():
    # val: 37
   print("hello world")
""")
with open("data/module_a.py", "r") as f:
    print(f.read())
    # out: def hello():
    # out:    print("hello world")

with open("data/module_b.py", "w") as f:
    f.write(r"""from data.module_a import hello
    # val: 40
hello()
""")
with open("data/module_b.py", "r") as f:
    print(f.read())
    # out: from data.module_a import hello
    # out: hello()
with open("data/module_b.py", "r") as f:
    exec(f.read())
    # val: None



#cmd("python", "data/module_b.py")

#cmd("python", "-m", "data.module_b")

make_file("data/__init__.py","")
# val: PosixPath('/home/runner/workspace/data/__init__.py')
cmd("python", "data/module_b.py")
# out: Traceback (most recent call last):
# out:   File "/home/runner/workspace/data/module_b.py", line 1, in <module>
# out:     from data.module_a import hello
# out: ModuleNotFoundError: No module named 'data'
cmd("python", "-m", "data.module_b")
# out: hello world


import os

os.system("python -m data.module_b")
# val: 0
######################################################################
import subprocess
subprocess.run(["python", "-m", "data.module_b"])
# val: CompletedProcess(args=['python', '-m', 'data.module_b'], returncode=0)
##########################
result = subprocess.run(
  ["python","-m", "data.module_b.py"],
  capture_output=True,
  text=True,
)
print(result.stdout)
# out: hello world
##########################




cmd("date")
# out: Thu Apr 30 12:08:09 PM UTC 2026
lsalf()
# out: total 88
# out: drwxr-xr-x 1 runner runner  462 Apr 30 12:08 ./
# out: drwxrwxrwx 1 runner runner   58 Apr 30 05:50 ../
# out: drwxr-xr-x 1 runner runner    0 Apr 16 10:23 .agents/
# out: drwxr-xr-x 1 runner runner   42 Apr 30 01:38 .cache/
# out: -rw------- 1 runner runner 4322 Apr 30 06:36 cs2520_lec13_exceptions_exercises.md
# out: -rw------- 1 runner runner 4090 Apr 30 06:44 cs2520_lec13_exercises (2).md
# out: drwxr-xr-x 1 runner runner  150 Apr 30 12:00 data/
# out: -rw-r--r-- 1 runner runner 9927 Apr  2  2025 generated-icon.png
# out: drwxr-xr-x 1 runner runner  172 Apr 30 12:07 .git/
# out: -rw-r--r-- 1 runner runner 3077 Feb 27  2024 .gitignore
# out: -rw-r--r-- 1 runner runner 2445 Apr 30 11:17 goog (copy).py
# out: -rw-r--r-- 1 runner runner 1926 Apr 30 12:08 goog.py
# out: drwxr-xr-x 1 runner runner   44 Apr 30 09:59 Helpers/
# out: -rw-r--r-- 1 runner runner 9929 Apr 30 09:55 inline_output_v3.py
# out: drwxr-xr-x 1 runner runner   84 Apr 30 09:54 .local/
# out: -rw------- 1 runner runner   75 Apr 30 09:53 main.py
# out: drwxr-xr-x 1 runner runner  542 Apr 30 10:39 old/
# out: drwxr-xr-x 1 runner runner  186 Apr 30 09:56 __pycache__/
# out: -rw-r--r-- 1 runner runner  157 Oct 31  2024 pyproject.toml
# out: drwxr-xr-x 1 runner runner   86 Jul 23  2025 .pythonlibs/
# out: -rw------- 1 runner runner  658 Apr 30 03:53 .replit
# out: drwxr-xr-x 1 runner runner   60 Apr 30 03:52 .upm/
# out: -rw-r--r-- 1 runner runner  122 Oct 31  2024 uv.lock







