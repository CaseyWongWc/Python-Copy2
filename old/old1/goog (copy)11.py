from Helpers.helpings import *


make_dir("test")
# val: PosixPath('/home/runner/workspace/test')
make_file("test/hello.txt", "Hello, World!")
# val: PosixPath('/home/runner/workspace/test/hello.txt')

print("Hello, World!")
# out: Hello, World!

remove_path("test")
# val: PosixPath('/home/runner/workspace/test')


make_file(
# val: PosixPath('/home/runner/workspace/test/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/hello.txt')
    "test/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/hello.txt",
    "Hello, World!",
)
remove_path("test")
# val: PosixPath('/home/runner/workspace/test')
INFO()
# out: /home/runner/workspace
# out: Thu Apr 30 12:41:14 PM UTC 2026
# out: ./.gitignore
# out: ./uv.lock
# out: ./pyproject.toml
# out: ./.upm/store.json1205111821
# out: ./.upm/store.json
# out: ./.pythonlibs/CACHEDIR.TAG
# out: ./.pythonlibs/.gitignore
# out: ./.pythonlibs/pyvenv.cfg
# out: ./generated-icon.png
# out: ./.replit
# out: ./.git/description
# out: ./.git/HEAD
# out: ./.git/FETCH_HEAD
# out: ./.git/COMMIT_EDITMSG
# out: ./.git/config
# out: ./.git/ORIG_HEAD
# out: ./.git/index
# out: ./__pycache__/inline_output.cpython-311.pyc
# out: ./__pycache__/inline_output_v2.cpython-311.pyc
# out: ./__pycache__/inline_output_v3.cpython-311.pyc
# out: ./__pycache__/main.cpython-311.pyc
# out: ./old/goog (copy).py
# out: ./old/goog (copy)2.py
# out: ./old/goog (copy)3.py
# out: ./old/example.txt
# out: ./old/greeting.txt
# out: ./old/log.txt
# out: ./old/MEEEEOWWWWWW.txt
# out: ./old/names.txt
# out: ./old/notes.txt
# out: ./old/sample.txt
# out: ./old/score.txt
# out: ./old/goog (copy)4.py
# out: ./old/real.txt
# out: ./old/inline_output.py
# out: ./old/goog (copy)5.py
# out: ./old/goog (copy)6.py
# out: ./old/inline_output_v2.py
# out: ./old/goog (copy)8.py
# out: ./old/goog (copy)9.py
# out: ./old/goog (copy)10.py
# out: ./old/goog (copy)7.py
# out: ./cs2520_lec13_exceptions_exercises.md
# out: ./cs2520_lec13_exercises (2).md
# out: ./data/real.txt
# out: ./data/real.py
# out: ./data/Square.py
# out: ./data/module_a.py
# out: ./data/__init__.py
# out: ./data/module_b.py
# out: ./Helpers/helpings.py
# out: ./inline_output_v3.py
# out: ./main.py
# out: ./goog.py

