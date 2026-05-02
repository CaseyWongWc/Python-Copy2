# sandbox_drafts/ — Agent's work-in-progress copy

This folder is the **agent's private copy** of the v6 sandbox runner.
It exists so the agent can build new features without touching
`sandbox/`, which is where Casey edits and where his GitHub pushes
land.

## Layout

```
sandbox_drafts/
├── README.md                      ← this file
├── inline_output_v6.py            ← work-in-progress runner
├── _smoke_test_run.py             ← copies of the 4 smoke tests so
├── _smoke_test_save_run.py            new features can be verified
├── _smoke_test_save_run_run.py        without touching sandbox/
└── _smoke_test_indent_fix.py
```

Notebook files (`goog.py`, `Helpers/`, etc.) and the runtime output
folder (`files/`) are NOT mirrored — those are Casey's coursework and
ephemeral output, both of which live only in `sandbox/`.

## Workflow

1. Casey works in `sandbox/` (and pushes/pulls from GitHub there).
2. Agent works on new runner features in `sandbox_drafts/`.
3. Smoke tests in `sandbox_drafts/` verify changes in isolation
   (each test imports `inline_output_v6` from its own directory).
4. When a feature is ready and Casey wants it, he pulls just the
   relevant pieces from `sandbox_drafts/` into `sandbox/` — usually
   a `cp sandbox_drafts/inline_output_v6.py sandbox/` after
   reviewing the diff, plus copying any new smoke tests.

## How to run a smoke test from this folder

```bash
python3 sandbox_drafts/_smoke_test_indent_fix.py
```

Each smoke test does `sys.path.insert(0, str(HERE))` so it imports
the **co-located** `inline_output_v6.py`, not the one in `sandbox/`.

## How to bring changes into sandbox/

Quick form (overwrite-and-go):

```bash
cp sandbox_drafts/inline_output_v6.py sandbox/inline_output_v6.py
cp sandbox_drafts/_smoke_test_*.py    sandbox/
```

Careful form (review first):

```bash
diff -u sandbox/inline_output_v6.py sandbox_drafts/inline_output_v6.py | less
```
