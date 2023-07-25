
# input_mode = num_a = num_b = None # 해주면 좋음

class Calculator:
# 다 쪼개기
    def input_modes():
        mode = ["plus", "minus","multiply","division","quit"]
        input_mode = input("연산모드를 입력시오. (plus / minus / multiply / division / quit):")
        # 이 코드도 너무 반복적
        if (input_mode not in mode):
        #     print("올바른 모드")  if (input_mode in mode): 이렇게 짜면 두줄이나 사용해야 함
        # else:
            print("알 수 없는 연산모드가 입력되었습니다.", mode)
            input_mode = input_modes()  #그냥 input_modes() 아님

    def input_num_a():
        try:
            num_a = int(input("숫자 1을 입력하시오. : ")) # 문자로 읽기 때문에 int로 변환해줘야 함 
        except ValueError:
            print("올바른 숫자가 입력되지 않았습니다.")
            print("다시 입력해주세요.")
            num_a = input_num_a()

    def input_num_b():
        try:
            num_b = int(input("숫자 2를 입력하시오. : "))
        except ValueError:
            print("올바른 숫자가 입력되지 않았습니다.")
            print("다시 입력해주세요.")
            num_b = input_num_b()

    def calc_value(mode, num_a, num_b):
        # try:
        # input_modes()
        # input_num_a()
        # input_num_b()
        # except ValueError: # 어떤 오류인지 정확히 알려줘야 함(숫자를 넣어야 하는데 글자 넣은 경우 출력)
        #     print("올바른 숫자가 입력되지 않았습니다.")
        #     print("다시 입력해주세요.")
        #     calc_value() # 처음에 input_values() 넣어서 안됐음 
        #     # exit(1) #except:로 만들경우 오류나면 불필요하게 사용자에게 주지 말고 프로그램 종료


        result = None #처음에 result 선언해놔야 좋음

        if mode == "plus":
            result = num_a + num_b
        elif mode == "minus":
            result = num_a - num_b
        elif mode == "multiply":
            result = num_a * num_b
        elif mode == "division":
            result = num_a / num_b
            try: #0으로 나눌때 에러
                result = num_a / num_b
            except ZeroDivisionError:
                print("0으로 나눗셈을 할 수 없습니다.")
                result = "NaN"
        else:
            print("연산모드를 정확히 입력하세요")
        return result

    if __name__ == "__main__": 
        # 모드가 quit 일떄까지 계속 이 계산기를 반복한다..
        while (True):
            mode = input_modes()
            if (mode == "quit"):
                break
            num1 = input_num_a()
            num2 = input_num_b()
            result = calc_value(mode, num1, num2)
        
        print("결과", result)


Calculator1=Calculator()
Calculator()#???




 


