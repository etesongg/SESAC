data = "게맛살 구멍 글라이더 기차 대롱 더치페이 도리 롱다리 리본 멍게 박쥐 본네트 빨대 살구 양심 이빨 이자 자율 주기 쥐구멍 차량 차박 트라이앵글"
data_list = data.split()

first_word = "기차"
empty_list = [first_word] 
user_word = []

print("<시작>끝말잇기를 하자. 내가 먼저 말할게. : " + first_word)

while 1:
    user_input = input()

    if user_input == "졌다":
        print('야호!')
        break
    elif user_input[0] != empty_list[-1][-1]:
        print('글자가 안 이어져. 내가 이겼다!')
        break
    elif user_input in empty_list: 
        print('아까 했던 말이야. 내가 이겼어!')
        break
    
    else: # user가 올바른 규칙으로 단어를 이었다면
        empty_list.append(user_input)
        rest_list = []
        for word in data_list: # data에서 사용한 단어를 뺀 나머지 단어 list 만들기
            if word not in empty_list: # word가 사용한 단어가 아니면 
                rest_list.append(word) 

        for word in rest_list:
            if word[0] == user_input[-1]: # word의 첫 글자와 user_input의 마지막 글자 비교
                rest_list = word

        if not rest_list: # 나머지 단어가 없을때
            print('모르겠다. 내가 졌어.')
            break
        else: #나머지 단어가 있을때
            print(rest_list)
            empty_list.append(rest_list) # 사용한 단어 리스트에 방금 사용한 단어를 추가해줌
            continue

# 사용한 단어는 empty_list 빈리스트에 넣어줌
# 사용할 수 있는 단어는 rest_list 나머지 리스트에 넣어줌





