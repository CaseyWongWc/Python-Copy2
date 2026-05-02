file_name = input()
lower_bound = input()
upper_bound = input()

with open(file_name, "r") as f:
    words = f.readlines()

for word in words:
    word = word.strip()  # Remove any leading/trailing whitespace
    if lower_bound <= word <= upper_bound:
        print(f"{word} - in range")
    else:
        print(f"{word} - not in range")
