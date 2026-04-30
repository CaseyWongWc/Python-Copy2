# 🐍 Lec_13 File I/O — Active Exercises

**How to use:**
1. Type each exercise into a `.py` file in Replit mobile
2. Save
3. Run `python inline_output.py yourfile.py`
4. Open the file → outputs appear as `# out:` comments
5. If output matches "Expected" below — ✅ understood

---

## Exercise 1 — Write your first file (5 min)

```python
# Open in WRITE mode → creates the file (or wipes existing)
outfile = open("notes.txt", "w")
outfile.write("Hello from Casey\n")
outfile.write("Line two\n")
outfile.close()

# Verify it worked by reading back
infile = open("notes.txt", "r")
content = infile.read()
infile.close()
print(content)
```

**Expected output:**
```
# out: Hello from Casey
# out: Line two
```

**Concept:** `'w'` = write (wipes), `'r'` = read, always `.close()`

---

## Exercise 2 — Append vs Write (5 min)

```python
# Append mode 'a' adds to end, doesn't wipe
outfile = open("log.txt", "w")
outfile.write("first line\n")
outfile.close()

# Reopen in APPEND mode
outfile = open("log.txt", "a")
outfile.write("appended line\n")
outfile.close()

infile = open("log.txt", "r")
print(infile.read())
infile.close()
```

**Expected output:**
```
# out: first line
# out: appended line
```

**Concept:** `'w'` wipes existing content. `'a'` keeps it, adds to bottom.

**Try the gotcha:** Run it twice. Does the file grow or stay the same? Why?

---

## Exercise 3 — Read line by line (5 min)

```python
# Setup
outfile = open("names.txt", "w")
outfile.write("Alice\n")
outfile.write("Bob\n")
outfile.write("Casey\n")
outfile.close()

# Read with a for loop (cleanest way!)
infile = open("names.txt", "r")
for line in infile:
    print(line.strip())  # .strip() removes the \n
infile.close()
```

**Expected output:**
```
# out: Alice
# out: Bob
# out: Casey
```

**Concept:** `for line in file:` reads one line at a time. `.strip()` removes trailing newline.

---

## Exercise 4 — `with` statement (the modern way) (5 min)

```python
# 'with' auto-closes the file even if something crashes
with open("greeting.txt", "w") as f:
    f.write("Hi from Lec 13\n")

# Read it back, also using 'with'
with open("greeting.txt", "r") as f:
    text = f.read()

print(text)
print("file is auto-closed now")
```

**Expected output:**
```
# out: Hi from Lec 13
# out: 
# out: file is auto-closed now
```

**Concept:** `with open(...) as f:` is the **preferred** way. No need to call `.close()` — it happens automatically.

**Why it matters:** If your code crashes between `open()` and `close()`, the file stays open and you can lose data. `with` prevents that.

---

## Exercise 5 — Numeric data needs str() conversion (5 min)

```python
# Files only store STRINGS. Numbers must be converted both ways.
score = 95
name = "Casey"

with open("score.txt", "w") as f:
    f.write(name + "\n")
    f.write(str(score) + "\n")  # int must become str!

# Reading back: str → int with int()
with open("score.txt", "r") as f:
    read_name = f.readline().strip()
    read_score = int(f.readline().strip())  # str → int

print(read_name)
print(read_score + 5)  # do math to prove it's an int
```

**Expected output:**
```
# out: Casey
# out: 100
```

**Concept:** Files store text only. Always `str()` to write numbers, `int()` or `float()` to read them back.

**Common bug:** Forgetting `int()` and getting `"95" + 5` → TypeError.

---

## Quick reference (post-exercises)

| Mode | What it does | Creates if missing? |
|---|---|---|
| `'r'` | Read only | ❌ FileNotFoundError |
| `'w'` | Write (wipes existing!) | ✅ |
| `'a'` | Append (adds to end) | ✅ |

| Method | Use |
|---|---|
| `f.write(s)` | Write string `s` |
| `f.read()` | Read whole file as one string |
| `f.readline()` | Read one line |
| `f.readlines()` | Read all lines as list |
| `for line in f:` | Loop line-by-line (best for big files) |

---

## After Exercises 1-5 → Ping me for:

- Exception handling (Lec_13 part 2 — pages 32-64)
- Combining files (read one, write to another)
- Or just sleep — these 5 = solid Lec_13 baseline

🌱 type slow, hit save, watch outputs land. you got this.
