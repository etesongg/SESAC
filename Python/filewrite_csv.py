# csv 파일을 알아야 함
import csv

data = [
    ("name", "age","city"),
    ("john", 25, "seoul"),
    ("bill", 20, "busan"),
    ("kim", 22, "seoul")
]

with open("user.csv", "w", newline='') as file: #newline이 찍히면 newline=''
    csv_file = csv.writer(file)
    csv_file.writerows(data) # 알아서 콤마 찍어주는 

print("csv write done")