# # try-except 예외처리

# numbers = [1, 2, 3, 4, 5]

# value = numbers[1]

# def get_number(index):
#     try:
#         # 오류 발생 가능성이 있는 코드 블록
#         return numbers[index]
#     except IndexError:
#         # 오류에 대한 처리 방법
#         print("입력값에 대한 인덱스 번호가 잘못되었습니다.")
#     except TypeError:
#         # 오류에 대한처리 방법
#         print("데이터 입력값의 유형이 잘못 되었습니다..")


# print(get_number(0))
# print(get_number(3))
# print(get_number(2))
# print(get_number(5))
# print(get_number('a'))

# 미션1. 글자를 입력받아 숫자로 변환해서 반환하시오.
# 미션1-2. 입력받은 글자를 숫자로 변환해서 +1 을 더해서 반환하시오.
# 미션2. 사용자로부터 입력받아
def convert_to_integer(str):
    value = None # value =0 이걸 추가하면 0 값으로 나옴

    try:
        value = int(str) + 1 # 중간 return 안 좋음 값주고 마지막에 return
    except ValueError:
        print("변환할수 없는 입력값 입니다.")
   
    return value



print(convert_to_integer("10"))
print(convert_to_integer("-5"))
print(convert_to_integer("7"))
print(convert_to_integer("A"))
print(convert_to_integer("Hello"))


