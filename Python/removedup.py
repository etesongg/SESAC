data1 = [1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6, 5]

# 미션1. 입력받은 값에서 중복을 제거하시요.
# 미션2. 아래 내용을 한줄로 작성하시오. (파이썬 기능/함수 최대한 사용해서)
def remove_duplicate(numbers): #미션1
        unique_list =[]
        for n in numbers:
            if n not in unique_list:# 없으면 추가
                  unique_list.append(n)
        return unique_list

def remove_duplicate2(numbers): #미션2
      return list(set(numbers))

unique_list = remove_duplicate2(data1)

print("원본리스트: ", data1)
print("유닉리스트: ", unique_list)


