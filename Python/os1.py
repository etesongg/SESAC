# 시스템 입출력
import os

current_dir = os.getcwd() # cwd(current working directory)
print("내 현재 폴더(디렉토리) : ", current_dir)


# os.mkdir() 파일 생성 
# new_dir = "sesac_1234"
# os.mkdir(new_dir) # make directory

# for i in range(0,10):
#     os.mkdir("sesac_" + str(i))

# for i in range(0,10):
#     os.rmdir("sesac_" + str(i)) # os.rmdir은 내용이 없어야 삭제 됨


# os.getenv() 환경변수 출력
# python_path = os.getenv("PYTHONPATH")
# print("윈도우 내의 PYTHONPATH 환경변수값 출력 : ", python_path)    


# os.system() 시스템 창 띄우기
my_commands = ["explorer", "calc"]  
for com in my_commands:
    os.system(com)