# 튜플 (a,b)
def get_name_and_age():
    return "John", 20

name, age = get_name_and_age()
print(name)
print(age)

# 리스트 - 배열[]
shopping_list = ["apple","banana","oriange"]
print(shopping_list)
shopping_list.append("grape")
print(shopping_list)
shopping_list.remove("banana")
print(shopping_list)

# 딕셔너리 활용(key-value)
# {"이름": "정송희"}
student = {
    "name": "John",
    "age": 20,
    "university": "ABC uni"
}

print("Name: ",student["name"])
print("Age: ",student["age"])

#-------------------

numbers = [1,2,3,4,5]

for num in numbers:
    if num % 2 ==0:
        print(num, "is 짝수")
    else:
        print(num, "is 홀수")

even_numbers=[]
odd_numvers=[]
for num in numbers:
    if num % 2 ==0:
        #print(num, "is 짝수")
        even_numbers.append(num)
    else:
        #print(num, "is 홀수")
        odd_numvers.append(num)

print(even_numbers)
print(odd_numvers)


# -------------------

student_grades = {"A": 20,
                "B": 45,
                "c": 90}

for student, grade in student_grades.items():
    if grade >= 90:
        print(student)

    # 90점 이상인 이름 불러오기 
