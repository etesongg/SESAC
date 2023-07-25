# 사용자로부터 점수 입력받기
# 사용자로부터 이름 입력받기
# 이 점수가 최고점수면 하이스코어 기록
# 미션1. 'high'라고 입력하면 현재까지의 하이스코어와 그 사람이 누군지 출력한다
# 미션2. 'history' 라고 입력하면 그동안 입력한 모든 점수와 사람을 출력한다

#-----------------------
#전역변수
#-----------------------
game_history =[] #어디서든 불러오는 전역변수 필요
highscore = 0

#-----------------------
#각종함수
#-----------------------
def input_value():
    score = int(input("점수를 입력하세요 : "))
    name = input("이름을 입력하세요 : ")
    
    return score, name


def store_result(score, name):
    game_score = (score, name) # 튜플 / {score, name}딕셔너리로 묶을수도 있음
    game_history.append(game_score)
    if (score > highscore):
        highscore = score

def print_history():
    print(game_history)

def print_highscore(highscore):
        print("최고점수 ",highscore)
    # for score, _ in game_history:
    #     # print(score[0]) # print(score)면 (10,aa) (20,f) , 지금은 10,20
    #     if score > highscore:
            # highscore = score

    # 점수가 많아지면 매번 수행하는 연산량이 많아짐 고치기
    
    # print("최고점수 :", highscore)


def input_mode():
    mode_ops = ["score", "history", "high"]
    mode = input("입력모드 (score, history, high): ")
    if mode not in mode_ops:
        mode = input("입력모드 : ")
    
    return mode


#-----------------------
# 메인함수
#-----------------------
# if __name__ == "__main__": 이렇게 해야 좋음
def main():
    while True:
        op = input_mode()
        if op == "score":
            score, name = input_value()
            store_result(score, name)
        elif op == "history":
            print_history()
        elif op == "high":
            print_highscore()


main() 











