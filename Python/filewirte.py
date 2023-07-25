# 파일 쓰기, 추가

data = "Hello world\n"
filename = "names.txt"

with open(filename, "a") as file:
    file.write(data)
print("파일 쓰기 완료")