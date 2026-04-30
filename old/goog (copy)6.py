from pathlib import Path
import shutil
import subprocess
import builtins

THEBASHCOMMANDS=None
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
    p.write_text(content, encoding="utf-8")
    # val: 3
    # val: 4
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
    # out: Thu Apr 30 09:20:00 AM UTC 2026
    if result.stderr:
        print(result.stderr)
    return result.returncode

def cmd(*cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    global THEBASHCOMMANDS
    THEBASHCOMMANDS=(result.stdout)
    if result.stderr:
        THEBASHCOMMANDS=(result.stderr)
    return result.returncode

def ret_file(path):
    p = ROOT / path
    return (p.read_text(encoding="utf-8"))

def list_project_files():
    return run_cmd("find", ".", "-maxdepth", "2", "-type", "f")
def lsalf():
    return run_cmd("ls","-alF")
##########################
#what is the time?
(run_cmd("date"))
# val: 0
here()
# val: PosixPath('/home/runner/workspace')
"oh"
1+1
# val: 2
make_file("folder1/folder2/file.txt","yea")
# val: PosixPath('/home/runner/workspace/folder1/folder2/file.txt')
ret_file(make_file("folder1/folder2/file.txt","yeah"))
# val: 'yeah'


cmd("ls","-alF")
# val: 0
##########################
print(THEBASHCOMMANDS)
# out: total 68
# out: drwxr-xr-x 1 runner runner  448 Apr 30 09:20 ./
# out: drwxrwxrwx 1 runner runner   58 Apr 30 05:50 ../
# out: drwxr-xr-x 1 runner runner    0 Apr 16 10:23 .agents/
# out: drwxr-xr-x 1 runner runner   42 Apr 30 01:38 .cache/
# out: -rw------- 1 runner runner 4322 Apr 30 06:36 cs2520_lec13_exceptions_exercises.md
# out: -rw------- 1 runner runner 4090 Apr 30 06:44 cs2520_lec13_exercises (2).md
# out: drwxr-xr-x 1 runner runner   16 Apr 30 08:41 data/
# out: drwxr-xr-x 1 runner runner   14 Apr 30 09:20 folder1/
# out: -rw-r--r-- 1 runner runner 9927 Apr  2  2025 generated-icon.png
# out: drwxr-xr-x 1 runner runner  172 Apr 30 09:19 .git/
# out: -rw-r--r-- 1 runner runner 3077 Feb 27  2024 .gitignore
# out: -rw-r--r-- 1 runner runner 1450 Apr 30 09:20 goog.py
# out: drwxr-xr-x 1 runner runner   22 Apr 30 09:19 Helpers/
# out: -rw-r--r-- 1 runner runner 9682 Apr 30 08:11 inline_output_v2.py
# out: drwxr-xr-x 1 runner runner   84 Apr 30 03:52 .local/
# out: -rw------- 1 runner runner   75 Apr 30 08:13 main.py
# out: drwxr-xr-x 1 runner runner  384 Apr 30 09:18 old/
# out: drwxr-xr-x 1 runner runner  122 Apr 30 08:15 __pycache__/
# out: -rw-r--r-- 1 runner runner  157 Oct 31  2024 pyproject.toml
# out: drwxr-xr-x 1 runner runner   86 Jul 23  2025 .pythonlibs/
# out: -rw------- 1 runner runner  658 Apr 30 03:53 .replit
# out: drwxr-xr-x 1 runner runner   60 Apr 30 03:52 .upm/
# out: -rw-r--r-- 1 runner runner  122 Oct 31  2024 uv.lock
