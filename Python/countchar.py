sentence = "Hello, world!"

#미션1. 원하는 글자 세기
def count_char(input_chr):
    count = 0
    for char in sentence:
        if char == input_chr:
            count = count + 1
            # count += 1
        

    return count

char = 'H'
count = count_char(char)
print(f"글자 {char} 갯수 : {count}")


def count_char2(text):
    count = 0
    for count_text in text:
        text.count()
    return count
text = input("글자를 입력하세요.: ")
print("글자 갯수 : ", count )


#미션2. 대소문자를 구분하지 않고 글자 세기

def count_char(input_char):
    count = 0
#채우기
#
#