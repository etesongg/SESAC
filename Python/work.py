users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},]

search_user = {
    "name": "Bob",
    "age": 30,
    "location": "Busan",
    #"car": "Mercedes"
}

def find_users(search_user):
    result = []
    isMatch = False
    for user in users:
        for key1, value1 in user.items():
            for key2, value2 in search_user.items():
                if key1 == key2 and value1 == value2:
                    isMatch = True                  
                    
    result.append(user)# 변수를 정의해서 isMatch = False if(isMatch)일때 result.append(user) / True, False 안 사용하면 or?이어서 맞는게 있는 갯수대로 나오는거 같음

    return result

print(find_users(search_user))


#강사님 답
def matches_criteria(user, condition):
    for key, value in condition.items():
            if user.get(key) != value:
                return False
            
    return True

def find_user(search_user):
    result = []
    for user in users:
        if matches_criteria(user, search_user):
            result.append(user)

    return result

#print(find_user(search_user))


#
# 케이스 모두 다 성공하면 PASS 하나라도 실패하면 FAIL


search_bob1 = { "name": "Bob"} #expect1
search_bob2 = { "age": 30} #expect1
search_bob3 = { "name": "Bob", "age": 30} #expect1
search_bob4 = { "name": "Bob", "age": 31} #expect1
search_bob5 = { } #expect3

# 리스트에 담자
#test_cases = [search_bob1, search_bob2, search_bob3, search_bob4, search_bob5]
#test_results = [1, 1, 1, 0, 3]

# test_results 리스트 따로 만들지 않고 작동시키기
test_cases = [{"case":search_bob1, "expected_result": 1}, 
              {"case":search_bob2, "expected_result": 1},
              {"case":search_bob3, "expected_result": 1},
              {"case":search_bob4, "expected_result": 0},
              {"case":search_bob5, "expected_result": 3}]

def test_find_users():
    Final_result = True
    
    # print(len(find_users(search_bob1)))
    # print(len(find_users(search_bob2)))
    # print(len(find_users(search_bob3)))
    # print(len(find_users(search_bob4)))
    # print(len(find_users(search_bob5)))
    
    # for test_case in test_cases:
    #     for find in len(test_case):
    #         for i in range (0,len(test_results)):
    #             test_results[i]
    #             if find == test_results[i]:
    #                 print('PASS')
    #             else:
    #                 print('FAIL')

        # for i, test_case in enumerate(test_cases):
        # # for i in range(0,len(test_cases)):
        #     if not len(find_users(test_cases[i])) == test_results[i]:
        #         Final_result = False

    for test_case in test_cases:
        if not len(find_users(test_case["case"])) == test_case["expected_result"]:
            Final_result = False


    # if not len((find_users(search_bob1))) == 1:
    #     Final_result = False
    # if not len((find_users(search_bob2))) == 1:
    #     Final_result = False
    # if not len((find_users(search_bob3))) == 1:
    #     Final_result = False
    # if not len((find_users(search_bob4))) == 0:
    #     Final_result = False
    # if not len((find_users(search_bob5))) == 3:
    #     Final_result = False

    if Final_result is True:
        print('PASS')
    else:
        print('FAIL')

test_find_users()

    
