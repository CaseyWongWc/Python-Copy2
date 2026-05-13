"""
Sandbox notebook runner.

Click Run on Replit (or `python sandbox/notebook/main.py` from anywhere).
This will:
  1. cd into sandbox/notebook/ so plain `open("name.txt")` calls in goog.py
     look there.
  2. Run inline_output_v6 against goog.py.

Convenience modes:
    - default: watch mode (auto-runs after edits settle)
    - --once:  run a single time and exit
    - --watch / --watch=<seconds>: force watch mode and set poll interval
    - --debounce=<seconds>: wait this long after edits before running
    - --error-backoff=<seconds>: cooldown after an error run
"""

import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SANDBOX_ROOT = HERE.parent

# So `import inline_output_v6` finds the module at <sandbox>/inline_output_v6.py
sys.path.insert(0, str(SANDBOX_ROOT))

# Run from the notebook dir so `open("foo.txt")` in goog.py looks here.
os.chdir(HERE)

from inline_output_v6 import run_and_annotate, _strip_old_annotations  # noqa: E402

TARGET = "goog.py"
DEFAULT_INTERVAL = 4.0
DEFAULT_DEBOUNCE = 3.0
DEFAULT_ERROR_BACKOFF = 10.0

# When True, strip annotations back out of goog.py after the magic-save copy
# (so goog.py returns to plain code). When False (default), annotations stay
# inlined in goog.py.
STRIP_AFTER_SAVE = False


def run_once() -> str:
    result = run_and_annotate(TARGET)
    print(result)
    if STRIP_AFTER_SAVE:
        p = Path(TARGET)
        p.write_text(_strip_old_annotations(p.read_text()))
    return result


def watch(
    interval: float = DEFAULT_INTERVAL,
    debounce: float = DEFAULT_DEBOUNCE,
    error_backoff: float = DEFAULT_ERROR_BACKOFF,
) -> None:
    p = Path(TARGET)
    last_cleaned = None
    changed_at = None
    next_allowed_run = 0.0

    print(f"Watching {TARGET} for changes (Ctrl+C to stop)...")
    print(
        f"Poll={interval}s, Debounce={debounce}s, ErrorBackoff={error_backoff}s"
    )

    while True:
        try:
            current_text = p.read_text()
        except FileNotFoundError:
            time.sleep(interval)
            continue

        current_cleaned = _strip_old_annotations(current_text)
        now = time.monotonic()

        if last_cleaned is None:
            result = run_once()
            last_cleaned = _strip_old_annotations(p.read_text())
            changed_at = None
            if "⚠️" in result or "# !err:" in result:
                next_allowed_run = now + error_backoff
        elif current_cleaned != last_cleaned:
            if changed_at is None:
                changed_at = now

            settled = (now - changed_at) >= debounce
            if settled and now >= next_allowed_run:
                result = run_once()
                last_cleaned = _strip_old_annotations(p.read_text())
                changed_at = None
                if "⚠️" in result or "# !err:" in result:
                    next_allowed_run = now + error_backoff
                else:
                    next_allowed_run = now
        else:
            changed_at = None

        time.sleep(interval)


if __name__ == "__main__":
    args = sys.argv[1:]

    watch_mode = True
    interval = DEFAULT_INTERVAL
    debounce = DEFAULT_DEBOUNCE
    error_backoff = DEFAULT_ERROR_BACKOFF

    for a in args:
        if a == "--once":
            watch_mode = False
        elif a == "--watch":
            watch_mode = True
        elif a.startswith("--watch="):
            watch_mode = True
            try:
                interval = float(a.split("=", 1)[1])
            except ValueError:
                print(f"Invalid --watch value. Using default {DEFAULT_INTERVAL}s.")
        elif a.startswith("--interval="):
            try:
                interval = float(a.split("=", 1)[1])
            except ValueError:
                print(f"Invalid --interval value. Using default {DEFAULT_INTERVAL}s.")
        elif a.startswith("--debounce="):
            try:
                debounce = float(a.split("=", 1)[1])
            except ValueError:
                print(f"Invalid --debounce value. Using default {DEFAULT_DEBOUNCE}s.")
        elif a.startswith("--error-backoff="):
            try:
                error_backoff = float(a.split("=", 1)[1])
            except ValueError:
                print(
                    f"Invalid --error-backoff value. Using default {DEFAULT_ERROR_BACKOFF}s."
                )

    try:
        if watch_mode:
            watch(interval=interval, debounce=debounce, error_backoff=error_backoff)
        else:
            run_once()
    except KeyboardInterrupt:
        print("\nStopped watcher.")
