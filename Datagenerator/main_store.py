import random
from datetime import date
import csv


# 클래스, 함수
class Load_file_data():
    @staticmethod
    def load_file(txt_file_name):
        with open(txt_file_name, "r", encoding='UTF8') as file: 
            lines = file.readlines()

        data = []
        for line in lines:
            data.append(line.strip())    
        return data
    
class Name_generate:
    def generate_name(self):
        type_name = random.choice(Load_file_data.load_file("store_types.txt"))
        dong_name = random.choice(Load_file_data.load_file("dongs.txt"))
        num = random.randint(1,100)
        return f"{type_name} {dong_name} {num}호점, {type_name}"

class Addr_generate:
    def generate_address(self):
        cities_kr = random.choice(Load_file_data.load_file("cities_kr.txt"))
        gu_kr = random.choice(Load_file_data.load_file("gu_kr.txt"))
        addr_num = random.randint(1, 100)
        addr_road = random.choice(["길", "로"])
        return f"{cities_kr} {gu_kr} {addr_num}{addr_road} {addr_num}"


    
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
                with open("store_info.csv", "w", newline='') as file:
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

class Store_generate:
    def __init__(self):
        self.name = Name_generate()  
        self.address = Addr_generate()

    def generate_data(self):
        data = []
        o = Printer()
        count = o.input_count() # Printer.input_count() : missing 1 required positional argument: 'self' 
        for _ in range(int(count)):
            name = self.name.generate_name()
            addr = self.address.generate_address()
            data.append(f"{name}, {addr}")

        Printer.output_type(data)



# 실행
store = Store_generate()
store.generate_data()










