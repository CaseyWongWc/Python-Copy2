from inline_output_v4 import run_and_annotate, _strip_old_annotations
from pathlib import Path
import sys
import time

TARGET = "goog.py"

# ── optional: clean annotations back out of goog.py after saving ─────────────
# goog.py is NEVER emptied — your code always stays there.
# When False (default): annotations stay inlined in goog.py after each run.
# When True:  annotations are stripped back out after the magic-comment save,
#             so goog.py returns to plain code, ready for the next problem.
STRIP_AFTER_SAVE = False
# ─────────────────────────────────────────────────────────────────────────────

def run_once() -> str:
    result = run_and_annotate(TARGET)
    print(result)

    if STRIP_AFTER_SAVE:
        p = Path(TARGET)
        p.write_text(_strip_old_annotations(p.read_text()))

    return result


def watch(interval: float = 4.0, debounce: float = 3.0, error_backoff: float = 10.0) -> None:
    p = Path(TARGET)
    last_cleaned = None
    changed_at = None
    next_allowed_run = 0.0
    print(f"Watching {TARGET} for changes (Ctrl+C to stop)...")
    print(f"Poll={interval}s, Debounce={debounce}s, ErrorBackoff={error_backoff}s")

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
            # Re-read after annotation so baseline matches what's in the file.
            last_cleaned = _strip_old_annotations(p.read_text())
            changed_at = None
            if "⚠️" in result or "# !err:" in result:
                next_allowed_run = now + error_backoff
        elif current_cleaned != last_cleaned:
            if changed_at is None:
                changed_at = now

            # Wait until edits settle so runs don't fire while you're typing.
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
            # File stabilized back to baseline.
            changed_at = None

        time.sleep(interval)


if __name__ == "__main__":
    args = sys.argv[1:]
    watch_mode = False

    interval = 4.0
    debounce = 3.0
    error_backoff = 10.0
    for a in args:
        if a == "--watch":
            watch_mode = True
        elif a.startswith("--watch="):
            watch_mode = True
            try:
                interval = float(a.split("=", 1)[1])
            except ValueError:
                print("Invalid --watch value. Using default 4.0s.")
        elif a.startswith("--interval="):
            try:
                interval = float(a.split("=", 1)[1])
            except ValueError:
                print("Invalid --interval value. Using default 4.0s.")
        elif a.startswith("--debounce="):
            try:
                debounce = float(a.split("=", 1)[1])
            except ValueError:
                print("Invalid --debounce value. Using default 3.0s.")
        elif a.startswith("--error-backoff="):
            try:
                error_backoff = float(a.split("=", 1)[1])
            except ValueError:
                print("Invalid --error-backoff value. Using default 5.0s.")

    try:
        if watch_mode:
            watch(interval=interval, debounce=debounce, error_backoff=error_backoff)
        else:
            run_once()
    except KeyboardInterrupt:
        print("\nStopped watcher.")
