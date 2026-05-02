import csv
with open("mycsv2.csv", "r") as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(row[1])
