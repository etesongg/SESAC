# 1부터 10까지의 각 숫자의 제곱으로 이루어진 목록을 만들때
squares = []
for x in range(1,10):
    squares.append(x ** 2)
print(squares)

# 제곱 더 쉽게 구현 하기 
squares[x ** 2] # 내가 원하는 것 정의하기
squares = [x ** 2 for x in range(1,11)] # 뒤에 내가 정의한 변수의 생성 방식 정의하기 
print(squares)

# 1부터 20까지의 짝수들로 리스트를 생성하시오
even_numbers = []
even_numbers = [x] # 내가 원하는 숫자를 표현할 정수
even_numbers = [x for x in range(1, 21)]
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

# 문자열의 각 글자를 순회하면서 대문자로 바꾸시오
word = "hello"
#upper_letters = [c]
upper_letters = [c for c in range(word)] # [c for c in range(word)print(word.upper())]
upper_letters = [c.upper() for c in range(word)]
print(upper_letters)

# 문자열 길이가 3이하인 단어들만 선택하기
words = ["apple", "banana", "cherry", "ragonfruit", "egg"]
short_words = []
#shrrt_words = [word]
short_words = [word.upper for word in words if len(word) <= 3]
print(short_words)