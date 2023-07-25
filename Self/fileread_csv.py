
import csv

with open("user.csv", "r", encoding='UTF8') as file: 
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
