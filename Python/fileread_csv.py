
import csv

with open("user.csv", "r") as file: #newline이 찍히면 newline=none
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
