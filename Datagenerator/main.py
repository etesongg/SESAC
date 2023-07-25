import random
from datetime import date
import csv

# names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
genders = ['Male', 'Female']


# 함수
def generate_name():
    with open("names.txt", "r") as file: 
        lines = file.readlines()

    names = []
    for line in lines:
        names.append(line.strip())

    return random.choice(names)

def generate_gender():
    return random.choice(genders)

def generate_birthdate():
    year_value = random.randint(1940,2015)
    month_value = random.randint(1,12)

    if month_value == 2:
        max_day_value = 28
    elif month_value in [4, 6, 9, 11]:
        max_day_value = 30
    else:
        max_day_value = 31

    day_value = random.randint(1,max_day_value)
    
    return f"{year_value}-{month_value:02d}-{day_value:02d}"

def calculate_age(birthdate):
    today = date.today()
    birthdate = date.fromisoformat(birthdate)
    age = today.year - birthdate.year + 1
    return age
 
def generate_address():
    with open("cities.txt", "r") as file: 
        lines = file.readlines()

    cities = []
    for line in lines:
        cities.append(line.strip())

    addr_num = random.randint(1,100)
    city = random.choice(cities)
    return f"{addr_num} {city}"

    


# 실행

data = []
for _ in range(10):
    name = generate_name()
    gender = generate_gender()
    birthdate = generate_birthdate()
    age = calculate_age(birthdate)
    addr = generate_address()
    data.append([name, gender, age, birthdate, addr])

with open("user_info.csv", "w", newline='') as file: 
    csv_file = csv.writer(file)
    csv_file.writerows(data)  

print("csv write done")





