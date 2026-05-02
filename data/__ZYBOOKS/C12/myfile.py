import csv
with open("myfile.csv", "r") as myfile:
    csv_reader = csv.reader(myfile) #✅<- 
    for row in csv_reader:
        print(row[1]) #✅<- 
        #⭐ out: Destination
        #⭐ out: Phoenix
        #⭐ out: Milan
        #⭐ out: London
