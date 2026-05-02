import csv

row1 = ["100", "50", "29"]
row2 = ["76", "32", "330"]

with open("gradeswr.csv", "w", newline="") as csvfile:
    grades_writer = csv.writer(csvfile)

    grades_writer.writerow(row1)
    grades_writer.writerow(row2)

    grades_writer.writerows([row1, row2])
#⭐ out: 100,50,29
#⭐ out: 76,32,330
#⭐ out: 100,50,29
#⭐ out: 76,32,330
# Feedback?
