import csv
with open("grades.csv", "r") as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=",")

    row_num = 1
    for row in grades_reader:
        print(f"Row #{row_num}: {row}")
        row_num += 1
#⭐ out: Row #1: ['name', 'hw1', 'hw2', 'midterm', 'final']
#⭐ out: Row #2: ['Petr Little', '9', '8', '85', '78']
#⭐ out: Row #3: ['Sam Tarley', '10', '10', '99', '100']
#⭐ out: Row #4: ['Joff King', '4', '2', '55', '61']
# Feedback?
