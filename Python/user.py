users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},]
"""
# 이름을 입력 받아 사용자 정보(딕셔너리)를 반납하시오
# 미션1. 이름을 입력 받아서 반납
# 미션2. 이름과 나이를 입력 받아서 반납
# 반납할 값의 종류가 1억개가 된다면,,, 어떻게 해야 편하게 할 수 있을까
search_user = {}
def find_users(name, age, location, car):
    result = []

    for user in users:
        if user["name"] == name and user["age"] == age:
            result.append(user)

    return result

result = find_users("Bob", 30)
result = find_users("John", 30)
result = find_users("Bob", 30)
result = find_users("Bob", 30)
#result = find_users("John")
print(result)
"""

# find_users 에서 계속 새로운 필드를 원할때마다, 인자값이 추가가 되어야 함
# 따라서 발생하는 문제가 기존에 사용중이던 모든 코드를 다 바꿔야 한다
# find_users(name, age) => find_users(name, age, location, car) 하면??
# 문제1. 어떻게 입력 인자를 효율적으로 받아서 처리하게 할까?

search_user = {
    "name": "Bob",
    "age": 30
}

search_bob = {
    "name": "Bob",
    "age": 30
}

def find_users(search_user):
    result = []

    for user in users:
        if user["name"] == search_user["name"] \
            and user["age"] == search_user["age"]:
            result.append(user)

    return result
result = find_users(search_bob)
print(result)
