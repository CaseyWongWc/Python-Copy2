from Helpers.helpings import *





make_file("folder1/folder2/file.txt","yeah")
# val: PosixPath('/home/runner/workspace/folder1/folder2/file.txt')
ret_file("folder1/folder2/file.txt")
# out: yeah
remove_path(here() / "folder1")
# val: PosixPath('/home/runner/workspace/folder1')
make_file("data/real.txt","hello\nworld")
# val: PosixPath('/home/runner/workspace/data/real.txt')
make_file("data/real.py",r"print('hello\nworld')")
# val: PosixPath('/home/runner/workspace/data/real.py')
ret_file("data/real.py")
# out: print('hello\nworld')
cmd("python", "data/real.py")
# out: hello
# out: world

make_file("data/real.txt","hello\nworld")
# val: PosixPath('/home/runner/workspace/data/real.txt')
ret_file("data/real.txt")
# out: hello
# out: world


cmd("date")
# out: Thu Apr 30 10:07:51 AM UTC 2026
lsalf()
# out: total 76
# out: drwxr-xr-x 1 runner runner  434 Apr 30 10:07 ./
# out: drwxrwxrwx 1 runner runner   58 Apr 30 05:50 ../
# out: drwxr-xr-x 1 runner runner    0 Apr 16 10:23 .agents/
# out: drwxr-xr-x 1 runner runner   42 Apr 30 01:38 .cache/
# out: -rw------- 1 runner runner 4322 Apr 30 06:36 cs2520_lec13_exceptions_exercises.md
# out: -rw------- 1 runner runner 4090 Apr 30 06:44 cs2520_lec13_exercises (2).md
# out: drwxr-xr-x 1 runner runner   44 Apr 30 10:06 data/
# out: -rw-r--r-- 1 runner runner 9927 Apr  2  2025 generated-icon.png
# out: drwxr-xr-x 1 runner runner  172 Apr 30 10:07 .git/
# out: -rw-r--r-- 1 runner runner 3077 Feb 27  2024 .gitignore
# out: -rw-r--r-- 1 runner runner  387 Apr 30 10:07 goog.py
# out: drwxr-xr-x 1 runner runner   44 Apr 30 09:59 Helpers/
# out: -rw-r--r-- 1 runner runner 9929 Apr 30 09:55 inline_output_v3.py
# out: drwxr-xr-x 1 runner runner   84 Apr 30 09:54 .local/
# out: -rw------- 1 runner runner   75 Apr 30 09:53 main.py
# out: drwxr-xr-x 1 runner runner  482 Apr 30 10:03 old/
# out: drwxr-xr-x 1 runner runner  186 Apr 30 09:56 __pycache__/
# out: -rw-r--r-- 1 runner runner  157 Oct 31  2024 pyproject.toml
# out: drwxr-xr-x 1 runner runner   86 Jul 23  2025 .pythonlibs/
# out: -rw------- 1 runner runner  658 Apr 30 03:53 .replit
# out: drwxr-xr-x 1 runner runner   60 Apr 30 03:52 .upm/
# out: -rw-r--r-- 1 runner runner  122 Oct 31  2024 uv.lock
