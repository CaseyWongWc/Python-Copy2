from pickle import GLOBAL
from pathlib import Path
import shutil
import subprocess
import builtins
import os


ROOT = Path.cwd()


def _queued_subprocess_stdin(cmd_args):
    """Return stdin text from notebook `# in:` queue for python subprocesses.

    The inline notebook runner replaces builtins.input with a shim carrying
    `_INPUTS` and `_input_consumed` in function globals. When a helper launches
    `python ...` as a child process, forward the newest reachable batch so child
    `input()` calls do not fall back to terminal stdin.
    """
    if not cmd_args:
        return None
    exe = str(cmd_args[0])
    if "python" not in exe:
        return None
    if os.environ.get("GOOG_NOTEBOOK_RUNNER") != "1":
        return None

    try:
        input_fn = builtins.input
        g = getattr(input_fn, "__globals__", None)
        if not isinstance(g, dict):
            return None
        raw_inputs = g.get("_INPUTS")
        consumed = g.get("_input_consumed")
        if not isinstance(raw_inputs, list) or not isinstance(consumed, list):
            return None
        if len(raw_inputs) != len(consumed):
            return None

        reachable = [
            i
            for i, item in enumerate(raw_inputs)
            if (not consumed[i]) and isinstance(item, (list, tuple)) and len(item) >= 3
        ]
        if not reachable:
            return None

        active_batch = max(raw_inputs[i][1] for i in reachable)
        selected = [i for i in reachable if raw_inputs[i][1] == active_batch]
        values = [str(raw_inputs[i][2]) for i in selected]
        if not values:
            return None

        # Mirror shim behavior: older reachable batches are stale once a newer
        # batch is used.
        for i in reachable:
            if raw_inputs[i][1] <= active_batch:
                consumed[i] = True

        return "\n".join(values) + "\n"
    except Exception:
        return None


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
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=ROOT,
        input=_queued_subprocess_stdin(cmd),
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode


def cmd(*cmd):
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=ROOT,
        input=_queued_subprocess_stdin(cmd),
    )
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


def INFO():
    return str(ROOT) + "\n" + cmd("date") + list_project_files()


def setin(*inputs):
    """
    A helper function to set test inputs for the input() function.
    Usage:
    setin("input1", "input2", "input3")
    This will set up the input() function to return "input1" on the first call,
    "input2" on the second call, and so on.
    To reset to normal input behavior, call setin() with no arguments or None:
    setin()
    """
    if inputs:
        input_iter = iter(inputs)

        def mock_input(prompt=""):
            try:
                value = next(input_iter)
                print(f"{prompt}{value}")
                return value
            except StopIteration:
                raise EOFError("No more inputs for testing")

        builtins.input = mock_input
    else:
        builtins.input = builtins._original_input_backup


def quiz(section_id, questions, prompt_label="Answer"):
    """
    Run a multi-question participation activity.

    questions = list of (question_text, expected_answer) tuples.
    Uses your existing setin() for staged inputs.

    Example:
        setin("True", "False", "True")
        quiz("11.1.2", [
            ("car_sticker_price", True),
            ("todays_temperature", False),
            ("inventory_quantity", True),
        ])
    """
    print(f"━━━ ✏️  Quiz {section_id} ━━━")
    correct = 0
    for i, (item, expected) in enumerate(questions, 1):
        try:
            answer = input(f"  {i}) {item}: ")
        except EOFError:
            print(f"  ⚠️  No more staged inputs at question {i}")
            break

        ok = str(answer).strip().lower() == str(expected).strip().lower()
        if ok:
            print(f"     ✅ Correct!")
            correct += 1
        else:
            print(f"     ❌ Got '{answer}', expected '{expected}'")

    total = len(questions)
    print(f"━━━ Score: {correct}/{total} ━━━\n")
    return correct, total
