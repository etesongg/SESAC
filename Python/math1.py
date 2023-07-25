import math

# 원의 넓이
radius = 5
area = (radius ** 2) * math.pi
area = math.pow(radius,2) * math.pi

print("원의 넓이 : ", area)

#----------------------------------
import random

#주사위 던지기

def roll_dice():
    dice_roll = random.randint(1, 6) #1,6 포함
    print(dice_roll)

for _ in range(1,11):
    roll_dice()


# 이 리스트를 무작위로 섞기
my_list = [1,2,3,4,5]

def shuffle():
    my_new_list = random.sample(my_list,5) #리스트 랜덤 추출
    return my_new_list

print("원본 리스트: ", my_list)
print("섞인 리스트: ", shuffle())

# 강사님.ver
random.shuffle(my_list) # 위에 함수 필요 없이 이것만 해도 됨
print("섞인 리스트: ", my_list)