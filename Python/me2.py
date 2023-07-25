import random

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

def generate_name():
    return random.choice(names)

def generate_gender():
    return None

def generate_birthdate():
	  return None

def generate_address():
    return None

data = []
for _ in range(10):
    name = generate_name()

for d in data:
    print(d)

generate_name()