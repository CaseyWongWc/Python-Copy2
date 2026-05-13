from pathlib import Path
import shutil
import subprocess
import builtins



ROOT = Path.cwd()

def here():
    return ROOT

def make_dir(path):
    p = ROOT / path
    p.mkdir(parents=True, exist_ok=True)
    return p

def make_file(path, content=""):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    # val: None
    # val: None
    # val: None
    # val: None
    p.write_text(content, encoding="utf-8")
    # val: 3
    # val: 4
    # val: 5
    # val: 11
    return p

def remove_path(path):
    p = ROOT / path
    if p.is_dir():
        shutil.rmtree(p)
    elif p.exists():
        p.unlink()
    return p

def run_cmd(*cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    print(result.stdout)
    # out: total 64
    # out: drwxr-xr-x 1 runner runner  434 Apr 30 08:46 ./
    # out: drwxrwxrwx 1 runner runner   58 Apr 30 05:50 ../
    # out: drwxr-xr-x 1 runner runner    0 Apr 16 10:23 .agents/
    # out: drwxr-xr-x 1 runner runner   42 Apr 30 01:38 .cache/
    # out: -rw------- 1 runner runner 4322 Apr 30 06:36 cs2520_lec13_exceptions_exercises.md
    # out: -rw------- 1 runner runner 4090 Apr 30 06:44 cs2520_lec13_exercises (2).md
    # out: drwxr-xr-x 1 runner runner   16 Apr 30 08:41 data/
    # out: drwxr-xr-x 1 runner runner   14 Apr 30 08:27 folder1/
    # out: -rw-r--r-- 1 runner runner 9927 Apr  2  2025 generated-icon.png
    # out: drwxr-xr-x 1 runner runner  172 Apr 30 08:46 .git/
    # out: -rw-r--r-- 1 runner runner 3077 Feb 27  2024 .gitignore
    # out: -rw-r--r-- 1 runner runner 1254 Apr 30 08:46 goog.py
    # out: -rw-r--r-- 1 runner runner 9682 Apr 30 08:11 inline_output_v2.py
    # out: drwxr-xr-x 1 runner runner   84 Apr 30 03:52 .local/
    # out: -rw------- 1 runner runner   75 Apr 30 08:13 main.py
    # out: drwxr-xr-x 1 runner runner  340 Apr 30 08:12 old/
    # out: drwxr-xr-x 1 runner runner  122 Apr 30 08:15 __pycache__/
    # out: -rw-r--r-- 1 runner runner  157 Oct 31  2024 pyproject.toml
    # out: drwxr-xr-x 1 runner runner   86 Jul 23  2025 .pythonlibs/
    # out: -rw------- 1 runner runner  658 Apr 30 03:53 .replit
    # out: drwxr-xr-x 1 runner runner   60 Apr 30 03:52 .upm/
    # out: -rw-r--r-- 1 runner runner  122 Oct 31  2024 uv.lock
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
    # out: ./.git/COMMIT_EDITMSG
    # out: ./.git/FETCH_HEAD
    # out: ./.git/config
    # out: ./.git/ORIG_HEAD
    # out: ./.git/index
    # out: ./__pycache__/inline_output.cpython-311.pyc
    # out: ./__pycache__/inline_output_v2.cpython-311.pyc
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
    # out: ./cs2520_lec13_exceptions_exercises.md
    # out: ./cs2520_lec13_exercises (2).md
    # out: ./data/real.txt
    # out: ./inline_output_v2.py
    # out: ./main.py
    # out: ./goog.py
    if result.stderr:
        print(result.stderr)
    return result.returncode
    
def ret_file(path):
    p = ROOT / path
    return (p.read_text(encoding="utf-8"))
    
def list_project_files():
    return run_cmd("find", ".", "-maxdepth", "2", "-type", "f")
def lsalf():
    return run_cmd("ls","-alF")
##########################
here()
# val: PosixPath('/home/runner/workspace')
run_cmd("ls","-alF")
# val: 0

make_file("folder1/folder2/file.txt","yea")
# val: PosixPath('/home/runner/workspace/folder1/folder2/file.txt')
make_file("folder1/folder2/file.txt","yeah")
# val: PosixPath('/home/runner/workspace/folder1/folder2/file.txt')

list_project_files()
# val: 0

ret_file("folder1/folder2/file.txt")
# val: 'yeah'
make_file("data/real.txt","hello")
# val: PosixPath('/home/runner/workspace/data/real.txt')
ret_file("data/real.txt")
# val: 'hello'
make_file("data/real.txt","hello\nworld")
# val: PosixPath('/home/runner/workspace/data/real.txt')
