import csv

file_name = input()

with open(file_name, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        words = row

counts = {}

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

for word in counts:
    print(f"{word} - {counts[word]}")