import random
from datetime import date
import csv


# 클래스, 함수
class Name_generate:
    def generate_name(self):
        last_name = random.choice(Load_file_data.load_file("last_names.txt"))
        first_name = random.choice(Load_file_data.load_file("first_names.txt"))
        return f"{last_name}{first_name}"

class Addr_generate:
    def generate_address(self):
        cities_kr = random.choice(Load_file_data.load_file("cities_kr.txt"))
        gu_kr = random.choice(Load_file_data.load_file("gu_kr.txt"))
        addr_num = random.randint(1, 100)
        addr_road = random.choice(["길", "로"])
        return f"{cities_kr} {gu_kr} {addr_num}{addr_road} {addr_num}"


class Load_file_data:
    @staticmethod 
    def load_file(txt_file_name):
        with open(txt_file_name, "r", encoding="UTF8") as file:
            lines = file.readlines()

        data = []
        for line in lines:
            data.append(line.strip())
        return data

class Gender_generate:
    def generate_gender(self):
        return random.choice(["Male", "Female"])


class Birthdate_generate:
    def generate_birthdate(self):
        year = random.randint(1940, 2015)
        month = random.randint(1, 12)

        if month == 2:
            max_day = 28
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        day = random.randint(1, max_day)

        return f"{year}-{month:02d}-{day:02d}"

class Age_calc:
    @staticmethod
    def calculate_age(birthdate):
        today = date.today()
        birthdate = date.fromisoformat(birthdate) # fromisoformat() 문자열을 date 객체로 변환 / (year, month, day)
        age = today.year - birthdate.year + 1
        return age

class Printer:
    def input_count(self):
        count = None
        try:
            count = int(input("데이터를 생성할 개수를 입력해주세요: "))
            if count < 0:
                raise ValueError()
        except ValueError:
            print("양수를 입력해주세요")
            count = self.input_count()
        
        return count

    @staticmethod
    def output_type(data):
        try:
            select_type = input("출력될 결과물 타입을 입력해주세요(console, csv): ")
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
            print("console, csv 중 하나를 정확하게 입력해주세요.")
            select_type = Printer.output_type(data)

class Human_generate:
    def __init__(self):
        self.name = Name_generate()  
        self.gender = Gender_generate()
        self.birthdate = Birthdate_generate()
        self.age = Age_calc()
        self.address = Addr_generate()

    def generate_data(self):
        data = []
        o = Printer()
        count = o.input_count() 
        for _ in range(int(count)):
            name = self.name.generate_name()
            gender = self.gender.generate_gender()
            birthdate = self.birthdate.generate_birthdate()
            age = self.age.calculate_age(birthdate)
            addr = self.address.generate_address()
            data.append(f"{name}, {gender}, {age}, {birthdate}, {addr}")

        Printer.output_type(data)


# 실행
human = Human_generate()
human.generate_data()

