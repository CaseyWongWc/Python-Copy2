import os

results = []

os.makedirs("test", exist_ok=True)

results.append(1 + 1)
results.append(1 + 2)
results.append(1 + 5)

with open("yes.py", "a") as f:
    f.write("\n\n# --- OUTPUT ---\n")
    for item in results:
        f.write("# " + str(item) + "\n")

# --- OUTPUT ---
# 2
# 3
# 4