from pickle import GLOBAL
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
    p.write_text(content, encoding="utf-8")
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
    if result.stderr:
        print(result.stderr)
    return result.returncode


def cmd(*cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.stderr:
        return result.stderr
    return result.stdout


def ret_file(path):
    p = ROOT / path
    return p.read_text(encoding="utf-8")


def list_project_files():
    return cmd("find", ".", "-maxdepth", "2", "-type", "f")


def lsalf():
    return cmd("ls", "-alF")
