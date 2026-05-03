# v7 Cheat Sheet (phone-friendly)

Pin this. Every shape, every gotcha, one page.

## The 4 block types

| Shape | What it does | Where it runs |
| --- | --- | --- |
| `with "FILE.ext":` | Saves body as raw file content | Nowhere (just writes) |
| `with Scratch:` (or `_` / `__`) | Runs body, throws away locals | In-process |
| `with Scratch as a:` | Runs body, keeps locals on `a` | In-process |
| `with RUN:` (or `Sandbox:`) | Runs body in a fresh subprocess | Subprocess |

## Combos (save + run, one block)

| Shape | What |
| --- | --- |
| `with "x.py" as Scratch:` | Save to x.py AND run in-process |
| `with "x.py" as a:` | Save to x.py AND run AND keep locals on `a` |
| `with "x.py" as RUN:` | Save to x.py AND run as subprocess |
| `with Scratch: "x.py"` | Reversed — same as `as Scratch` |
| `with Scratch as a: "x.py"` | Reversed — same as `as a` |
| `with bash:` | Run body as shell commands |

## Output annotations (auto-added)

- `# out: <line>`  — anything `print()` produced
- `# val: <repr>`  — bare-expression values (like `a` on its own line)
- `# err: <line>`  — stderr / traceback lines
- `# !err: <msg>`  — block-killing error or exit code
- `# a.out: <line>` — auto-show: every print under `as a:` mirrored here

All of these get stripped + re-spliced every run. Don't edit by hand.

## Feeding input

**TWO rules to remember:**

**Rule 1 — `# in:` placement depends on block type:**

| Block type | Where `# in:` goes |
| --- | --- |
| `with Scratch:` / `as a:` / in-process save+run | Anywhere (outside or inside body, both work) |
| `with RUN:` / `as RUN:` / subprocess | INSIDE body, indented |
| `with bash:` | Doesn't read `# in:` — pipe with `<<<` instead |

**Rule 2 — newer `# in:` shadows older:**

If you have `# in: 1` somewhere and forget about it, then later type `# in: 7` right before a new block, the new block gets `7` (not `1`). Stale leftovers get auto-dropped.

EXCEPTION: consecutive `# in:` lines (no code between, blanks/comments OK) are treated as ONE batch and consumed in order — so multi-input prompts still work:

```
# in: alice
# in: 30
with Scratch:
    name = input()  # gets alice
    age = input()   # gets 30
```

**Alt syntax:** `setin("a", "b", "c")` does the same thing as 3 `# in:` lines.

## Crash isolation

If a block raises an exception, you get `# !err: <type>: <msg>` + `at line N` right under the block, and the next block STILL runs. One bad block can't kill the notebook.

## Common patterns

```python
# Quick scratch
with Scratch:
    x = 5
    x * 2
    # val: 10

# Save a data file
with "data.txt":
    line one
    line two

# Save + run a script in-process
with "calc.py" as a:
    a, b = 3, 4
    print(a + b)
    # out: 7

# Save + run as real subprocess (closer to `python calc.py`)
with "calc.py" as RUN:
    # in: 5
    n = int(input())
    print(n * 2)
    # out: 10

# Verify what was written
with bash:
    cat calc.py
    python calc.py <<< "5"
```

## Reserved names

These can't be used as capture names (they have special meaning):
`Scratch`, `_`, `__`, `RUN`, `Sandbox`

So `with "x.py" as Sandbox:` = subprocess (RUN alias), but
`with "x.py" as a:` = in-process with locals on `a`.

## Gotchas (real ones I've hit)

1. **RUN doesn't share `# in:` with outside.** Outer `# in: 1` + `with "x.py" as RUN:` that calls `input()` → EOFError. Put the `# in:` INSIDE the RUN body.
2. **Variables don't carry between Scratch blocks.** Each `with Scratch:` is a fresh function scope. Use `as a:` and reference `a.x` later, OR write to a file.
3. **`# RUN out:` is legacy.** v7 just emits `# out:` for RUN blocks now. Old `# RUN out:` lines get auto-stripped on next run.
4. **Annotations inside `with "FILE":` body get stripped before save.** So they're cosmetic clutter only — won't poison the saved file.
