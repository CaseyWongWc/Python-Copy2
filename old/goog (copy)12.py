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


ret_file("goog.py")
# out: from Helpers.helpings import *
# out: 
# out: 
# out: make_dir("test")
# out: make_file("test/hello.txt", "Hello, World!")
# out: 
# out: print("Hello, World!")
# out: 
# out: remove_path("test")
# out: 
# out: 
# out: make_file(
# out:     "test/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/hello.txt",
# out:     "Hello, World!",
# out: )
# out: remove_path("test")
# out: 
# out: 
# out: ret_file("goog.py")
# out: 
# out: 
# out: ret_file("data/real.txt")
# out: 
# out: try:
# out:     print(1/0)
# out: except Exception as e:
# out:     print(e)
# out: try:
# out:     make_file("test/hello.py",r"""
# out:     ; se mi co lin
# out:     ♤●♤○○♤\■\€~•¥₩1°°°°°°🎃🎄🎆🧨✨️🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎟🎫°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°▪︎●🫨😲😯😲🫨😯\n\n\t
# out:     """)
# out:     ret_file("test/hello.py")
# out:     cmd("python","-m"," test/hello.py")
# out:     cmd("python","test/hello.py")
# out: except Exception as e:
# out:     print(e)
# out: finally:
# out:     remove_path("test")
# out:  
# out:                                
# out:                                             
# out: INFO()
# out: 
# out: 
# out: 
# out: 
# out: 
# out: 


ret_file("data/real.txt")
# out: hello
# out: world

try:
    print(1/0)
except Exception as e:
    print(e)
    # out: division by zero
try:
    make_file("test/hello.py",r"""
    # val: PosixPath('/home/runner/workspace/test/hello.py')
    ; se mi co lin
    ♤●♤○○♤\■\€~•¥₩1°°°°°°🎃🎄🎆🧨✨️🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎟🎫°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°▪︎●🫨😲😯😲🫨😯\n\n\t
    """)
    ret_file("test/hello.py")
    # out: 
    # out:     ; se mi co lin
    # out:     ♤●♤○○♤\■\€~•¥₩1°°°°°°🎃🎄🎆🧨✨️🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎟🎫°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°▪︎●🫨😲😯😲🫨😯\n\n\t
    # out:     
    cmd("python","-m"," test/hello.py")
    # out: /home/runner/workspace/.pythonlibs/bin/python: Error while finding module specification for ' test/hello.py' (ModuleNotFoundError: No module named ' test/hello'). Try using ' test/hello' instead of ' test/hello.py' as the module name.
    cmd("python","test/hello.py")
    # out:   File "/home/runner/workspace/test/hello.py", line 2
    # out:     ; se mi co lin
    # out: IndentationError: unexpected indent
except Exception as e:
    print(e)
finally:
    remove_path("test")
    # val: PosixPath('/home/runner/workspace/test')
 
                               
                                            
INFO()
# out: /home/runner/workspace
# out: Thu Apr 30 01:28:15 PM UTC 2026
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
# out: ./old/goog (copy)11.py
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






