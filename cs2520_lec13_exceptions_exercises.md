# 🚨 Lec_13 Part 2 — Exceptions (Active Exercises)

You already used `try/except` in your goog-1.py — you're ahead.
These 3 exercises lock in the rest: `else`, `finally`, multiple excepts, and `raise`.

---

## Exercise 6 — Multiple `except` blocks (catch different errors differently)

```python
def divide_and_convert(a, b, text):
    try:
        result = a / b
        number = int(text)
        print(f"result: {result}, number: {number}")
    except ZeroDivisionError:
        print("can't divide by zero!")
    except ValueError:
        print(f"can't turn '{text}' into a number!")

# Try it 3 ways
divide_and_convert(10, 2, "5")     # works
divide_and_convert(10, 0, "5")     # ZeroDivisionError
divide_and_convert(10, 2, "cat")   # ValueError
```

**Expected output:**
```
# out: result: 5.0, number: 5
# out: can't divide by zero!
# out: can't turn 'cat' into a number!
```

**Concept:** Different errors → different except blocks. Python checks them top-down, picks the matching one.

---

## Exercise 7 — `else` and `finally` (the full picture)

```python
def safe_open(filename):
    try:
        f = open(filename, "r")
        content = f.read()
    except FileNotFoundError:
        print(f"'{filename}' doesn't exist")
    else:
        # else = ONLY runs if try succeeded (no exception)
        print(f"got it: {content.strip()}")
        f.close()
    finally:
        # finally = ALWAYS runs, success or failure
        print(f"done trying with {filename}")
        print("---")

# Setup: make a real file first
with open("real.txt", "w") as f:
    f.write("hello!")

safe_open("real.txt")     # try succeeds → else runs, finally runs
safe_open("ghost.txt")    # try fails → except runs, finally runs
```

**Expected output:**
```
# out: got it: hello!
# out: done trying with real.txt
# out: ---
# out: 'ghost.txt' doesn't exist
# out: done trying with ghost.txt
# out: ---
```

**Concept:**
- `try:` — the risky code
- `except:` — runs IF an error happens
- `else:` — runs ONLY if NO error
- `finally:` — runs ALWAYS (cleanup)

**Why `finally` matters:** even if your code crashes, `finally` runs. Perfect for closing files, releasing locks, cleanup.

---

## Exercise 8 — `raise` (throw your own errors)

```python
def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("can't withdraw a negative amount")
    if amount > balance:
        raise ValueError(f"insufficient funds: have {balance}, want {amount}")
    return balance - amount

# Try with try/except to catch your own raised errors
try:
    new_balance = withdraw(100, 30)
    print(f"new balance: {new_balance}")
except ValueError as err:
    print(f"oops: {err}")

try:
    new_balance = withdraw(100, 999)
    print(f"new balance: {new_balance}")
except ValueError as err:
    print(f"oops: {err}")

try:
    new_balance = withdraw(100, -5)
    print(f"new balance: {new_balance}")
except ValueError as err:
    print(f"oops: {err}")
```

**Expected output:**
```
# out: new balance: 70
# out: oops: insufficient funds: have 100, want 999
# out: can't withdraw a negative amount   ← actually wait, no
# out: oops: can't withdraw a negative amount
```

**Concept:**
- `raise SomeError("message")` = throw your own error
- `except SomeError as err:` = catch it AND keep the message in `err`
- `f"oops: {err}"` = prints the message you wrote

**Why this matters:** real code uses `raise` to enforce rules. ("This input is bad — stop here.")

---

## Quick reference (post-exercises)

| Block | When it runs |
|---|---|
| `try:` | always (the risky part) |
| `except SomeError:` | only if SomeError was raised |
| `except:` (bare) | catches everything (use sparingly!) |
| `else:` | only if NO exception in try |
| `finally:` | ALWAYS, no matter what |

| Common errors | Caused by |
|---|---|
| `ZeroDivisionError` | `x / 0` |
| `ValueError` | `int("cat")`, bad data |
| `TypeError` | `f.write(1)` (your discovery!) |
| `FileNotFoundError` | open file that doesn't exist |
| `IndexError` | `lst[100]` when list has 5 items |
| `KeyError` | `d["missing_key"]` |

---

## After Ex 6-8 → you have:
- ✅ All of File I/O (Lec_13 part 1)
- ✅ All of Exceptions (Lec_13 part 2)
- ✅ Lec_13 = 100% covered, by hand

🌱 type slow. when ready to crash, crash. brain consolidates overnight.
