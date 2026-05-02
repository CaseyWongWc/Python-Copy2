import csv

file_name = input()

word_freq = {}
with open(file_name, "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        for word in row:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

for word, freq in word_freq.items():
    print(f"{word} - {freq}")
