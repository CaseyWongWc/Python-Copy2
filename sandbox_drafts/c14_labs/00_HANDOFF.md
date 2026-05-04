# C_14 Recursion — Handoff Notes

**Last updated:** 2026-05-04 ~2 AM PDT, by Comet on behalf of Casey
**Casey's status:** burnt out, going to sleep. Test on Thursday (3 days).
**Score:** 71/76 (Section 14.6 has 5 pts unfinished — see below).

---

## C_14 Section breakdown

| Section | Score | Status |
|---------|-------|--------|
| 14.1 | 6/6   | done before this session |
| 14.2 | 9/9   | done |
| 14.3 | 3/3   | done |
| 14.4 | 8/8   | done |
| 14.5 | 4/4   | done |
| 14.6 | 1/6   | **5 pts left — see below** |
| 14.7 LAB | 10/10 | done this session |
| 14.8 LAB | 10/10 | done this session |
| 14.9 LAB | 10/10 | done this session |
| 14.10 LAB| 10/10 | done this session |

---

## Unfinished — Section 14.6 (5 pts)

These are participation/challenge activities. Casey just needs to enter the answers — they're already known:

### 14.6.2 Participation (2 pts)
1. Output of `scramble("xy", "")` -> **`xy yx`**
2. Closest function to generate 3-letter subsets from N-letter word -> **`shopping_bag_combinations`**

### 14.6.1 Challenge Level 1 (1 pt) -- numbers 0, 6, 9
Drag in this order:
```
069
096
609
690
906
960
```

### 14.6.1 Challenge Level 2 (1 pt) -- reversed range, numbers 0, 6, 9
```
960
906
690
609
096
069
```
(numbers may differ if zyBooks regenerates -- pattern: each digit leads, two arrangements of remaining)

### 14.6.2 Challenge (1 pt) -- explore() drag-and-drop
Recursive case order:
```python
for i, val in enumerate(remain_vals):
    new_remain = remain_vals[:i] + remain_vals[i+1:]
    new_picked = picked_vals + [val]
    explore(new_remain, new_picked)
```

---

## LAB solutions (all verified)

All 4 LABs have working code in:
- `sandbox_drafts/c14_labs/14_7_fibonacci.py`
- `sandbox_drafts/c14_labs/14_8_permutations.py`
- `sandbox_drafts/c14_labs/14_9_number_pattern.py`
- `sandbox_drafts/c14_labs/14_10_count_digits.py`

Also pasted into `sandbox/notebook/goog.py` with full spec docstrings as section blocks.

---

## Recursion test cheat sheet (for Thursday's test)

### The 3 patterns we used:

**1. Linear recursion (Fibonacci, count digits):**
```python
def f(n):
    if base_case(n): return base_value
    return combine(f(n - 1))   # or f(n // 10), f(n - 2), etc.
```

**2. Print-recurse-print (number pattern, mirror):**
```python
def f(n):
    print(n)              # pre-order
    if base_case: return
    f(reduce(n))
    print(n)              # post-order, mirrors the descent
```

**3. Tree-of-choices recursion (permutations, scramble, subsets):**
```python
def explore(remain, picked):
    if len(remain) == 0:
        emit(picked)
        return
    for i in range(len(remain)):
        new_remain = remain[:i] + remain[i+1:]
        new_picked = picked + [remain[i]]
        explore(new_remain, new_picked)
```

### Common gotchas:
- zyBooks Fibonacci uses **fib(0)=0, fib(1)=1** (NOT fib(0)=1).
- Negative input to fib must return -1.
- Number-pattern stops when `num1 < 0` (not `<= 0`) to capture the negative middle.
- Permutations output uses `', '.join()` -- comma + space.
- digit_count(0) = 1.

---

## Files of interest for next agent / future Casey
- `sandbox/notebook/goog.py` -- master notebook with all spec blocks + runners
- `sandbox_drafts/c14_labs/` -- per-LAB clean solution files
- `sandbox/files/lab_14_8.py` -- mirrors 14_8_permutations.py
- `push_replit.sh` -- pushes everything to GitHub/Replit remote
