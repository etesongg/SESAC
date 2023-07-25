def print_coin():
    print("비트코인")

def print_coins():
    for i in range(100):
        print("비트코인")

def print_with_smile(str):
    print(str, ":D")


def print_sum(a,b):
    print(a+b)

def print_arithmetic_operation(a,b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

def print_max(a,b,c):
    max_val = a
    if max_val < b:
        max_val = b
        if max_val < c:
            max_val = c
    print(max_val)    


def print_reverse(str):
    print(str[::-1])


def print_score(score_list):
    print(sum(score_list)/len(score_list))


def print_even(even_list):
    for i in even_list:
        if i % 2 == 0:
            print(i)


def print_keys(dic_key):
    for i in dic_key.keys():
        print(i)

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}


def print_value_by_key(my_dict, key):
    print(my_dict[key])


def print_5xn(str):
    for i in range(0,len(str),5):
        print(str[i:i+5])

def print_mxn(str,num):
    for i in range(0,len(str),num):
        print(str[i:i+num])

def calc_monthly_salary(num):
    print(int(num/12))


def make_url(str):
    print(f"www.{str}.com")


def make_list(str):
    slice_list =[]
    for i in range(len(str)):
        slice_list.append(str[i])
    # print(slice_list)
    return slice_list


def pickup_even(pick_list):
    even_list = []
    for i in range(len(pick_list)):
        if pick_list[i] % 2 == 0:
            even_list.append(pick_list[i])
    return even_list

def convert_int (str):
    return int(str.replace(',', ''))


# f = open("C:/Users/songhee/Desktop/매수종목1.txt", mode="wt")
# f.write("005930\n")
# f.write("005380\n")
# f.write("035420")
# f.close()

# f = open("C:/Users/songhee/Desktop/매수종목2.txt", "w")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER")



per = ["10.31", "", "8.00"]

for i in per:
    
    try:
        print(float(i))
    except:
        print("실수가 아닙니다.")
    else:
        print("실수가 맞습니다.")
    finally:
        print("프로그램을 종료합니다.")
    





















