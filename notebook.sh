#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_PY="$ROOT_DIR/sandbox/notebook/main.py"

PYTHON_BIN="${PYTHON_BIN:-python3}"
WATCH_INTERVAL="${WATCH_INTERVAL:-4.0}"
DEBOUNCE="${DEBOUNCE:-3.0}"
ERROR_BACKOFF="${ERROR_BACKOFF:-10.0}"

print_usage() {
  cat <<'EOF'
Usage:
  ./notebook.sh                Run once (simple mode). If an error is detected, start slow watch mode.
  ./notebook.sh --once         Run once only, never auto-switch.
  ./notebook.sh --watch        Start slow watch mode now.
  ./notebook.sh --help         Show this help.

Optional env overrides:
  WATCH_INTERVAL=4.0
  DEBOUNCE=3.0
  ERROR_BACKOFF=10.0
  PYTHON_BIN=python3
EOF
}

run_once() {
  "$PYTHON_BIN" "$MAIN_PY" --once
}

run_watch() {
  exec "$PYTHON_BIN" "$MAIN_PY" \
    --watch="$WATCH_INTERVAL" \
    --debounce="$DEBOUNCE" \
    --error-backoff="$ERROR_BACKOFF"
}

if [[ ! -f "$MAIN_PY" ]]; then
  echo "main runner not found: $MAIN_PY" >&2
  exit 1
fi

mode="auto"
if [[ $# -gt 0 ]]; then
  case "$1" in
    --once)
      mode="once"
      ;;
    --watch)
      mode="watch"
      ;;
    --help|-h)
      print_usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      print_usage
      exit 2
      ;;
  esac
fi

if [[ "$mode" == "watch" ]]; then
  run_watch
fi

output="$(run_once 2>&1 || true)"
printf '%s\n' "$output"

if [[ "$mode" == "once" ]]; then
  exit 0
fi

# Auto mode: switch to watch only when the runner reports an error annotation.
if [[ "$output" == *"Had an error"* || "$output" == *"# !err:"* || "$output" == *"WARN"* || "$output" == *"⚠"* ]]; then
  echo
  echo "Error detected. Switching to slow watch mode (Ctrl+C to stop)."
  run_watch
fi
