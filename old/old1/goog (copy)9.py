from sys import stdout
from Helpers.helpings import *


class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        if new_side <= 0:
            raise ValueError("Side length must be positive")
        else:
            self.__side = new_side


test = Square(10)
print(test.side)
# out: 10
test.side = 20
print(test.side)
# out: 20

try:
    test.side = -10
except ValueError:
    print("a")
    # out: a
print(test.side)
# out: 20
# raise NameError("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

try:
    raise ValueError("hello")
except ValueError:
    print("hello")
    # out: hello
else:
    print("never")
finally:
    print("always")
    # out: always

try:
    raise ValueError(1 + 1)
except ValueError:
    print("hello")
    # out: hello
    pass
# raise Exception("boom")


cmd("date")
# out: Thu Apr 30 11:16:58 AM UTC 2026
lsalf()
# out: total 76
# out: drwxr-xr-x 1 runner runner  434 Apr 30 11:16 ./
# out: drwxrwxrwx 1 runner runner   58 Apr 30 05:50 ../
# out: drwxr-xr-x 1 runner runner    0 Apr 16 10:23 .agents/
# out: drwxr-xr-x 1 runner runner   42 Apr 30 01:38 .cache/
# out: -rw------- 1 runner runner 4322 Apr 30 06:36 cs2520_lec13_exceptions_exercises.md
# out: -rw------- 1 runner runner 4090 Apr 30 06:44 cs2520_lec13_exercises (2).md
# out: drwxr-xr-x 1 runner runner   62 Apr 30 10:30 data/
# out: -rw-r--r-- 1 runner runner 9927 Apr  2  2025 generated-icon.png
# out: drwxr-xr-x 1 runner runner  172 Apr 30 11:16 .git/
# out: -rw-r--r-- 1 runner runner 3077 Feb 27  2024 .gitignore
# out: -rw-r--r-- 1 runner runner  897 Apr 30 11:16 goog.py
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
