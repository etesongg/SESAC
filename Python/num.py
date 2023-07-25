data1 = [3, 7, 2, 9, 1, 4]
data2 = [-21, -34, -3, -45]

def find_max(numbers):
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max
    
print("최대값: " ,find_max(data1))

# 미션2. 사용자로부터 입력 받아서, 공백(스페이스)로 구분된 문자열을 입력 받아서
# 그 안에서 max를 구하시오
#input() 입력받아서 그 리스트 내에서 max

# 미션3. 리스트 컴프리헨션을 사용해서 위의 복잡한 과정을 한줄로 변경하시오.
def find_max2(text):
    numbers = [int(string)
               for string in text.split()]
    #numbers = []
    #strings = text.split()
    #for string in strings:
    #    numbers.append(int(string))

    return find_max(numbers)


user_input = input("숫자를 입력하시오(공백으로 구분): ")
max_number = find_max2(user_input)
print(max_number)