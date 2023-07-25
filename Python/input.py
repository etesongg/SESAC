# 사용자로부터 문자(문장)을 입력받아 대문자로 변환하시오
# 입력받은 문장에서 대문자는 소문자로, 소문자는 대문자로

def convert_case(text):
    result = ""
    for c in text:
        if c.islower():
            result +=c.upper()
        else:
            result +=c.lower()
    return result

# 실행 후 사용자로부터 입력받음    
text = input("문자열을 입력하세요.: ")
result = convert_case(text)
print("변환된 문장 : ", result)





