import random
from datetime import date
import csv

# names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
genders = ['Male', 'Female']


# 함수
def generate_name():
    return random.choice(load_file("names.txt"))

def generate_gender():
    return random.choice(genders)

def generate_birthdate():
    year = random.randint(1940,2015)
    month = random.randint(1,12)

    if month == 2:
        max_day = 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31

    day = random.randint(1,max_day)
    
    return f"{year}-{month:02d}-{day:02d}"

def calculate_age(birthdate):
    today = date.today()
    birthdate = date.fromisoformat(birthdate)
    age = today.year - birthdate.year + 1
    return age
 
def generate_address():
    addr_num = random.randint(1,100)
    city = random.choice(load_file("cities.txt"))
    return f"{addr_num} {city}"

def load_file(txt_file_name):
    with open(txt_file_name, "r") as file: 
        lines = file.readlines()

    data = []
    for line in lines:
        data.append(line.strip())
    
    return data

def input_count():
        try:
            count = int(input("데이터를 생성할 개수를 입력해주세오 : "))

            if count < 0:
                raise ValueError()
            else:
                return count
        except ValueError:
            print("양수를 입력해주세요")
            count = input_count()

def output_type(data):
        try:
            select_type = input("출력될 결과물 타입을 입력해주세요(console, csv) :")
            if select_type == "csv":
                with open("user_info.csv", "w", newline='') as file: 
                    csv_file = csv.writer(file)
                    csv_file.writerows(data)  

                print("csv write done")
            elif select_type == "console":
                print(data)
            else:
                raise ValueError()
        except ValueError:
            print("console, csv 중 하나를 정확하게 입력해주세요. ")
            select_type = output_type(data)


        

def main():
    data = []

    for _ in range(input_count()):
        name = generate_name()
        gender = generate_gender()
        birthdate = generate_birthdate()
        age = calculate_age(birthdate)
        addr = generate_address()
        data.append([name, gender, age, birthdate, addr])

    output_type(data)

    


# 실행
main()







