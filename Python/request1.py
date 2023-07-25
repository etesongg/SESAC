# 그러면 웹 페이지도 가져올 수 있을까?

import requests

# 추가 패키지 설치
# https://pypi.org/

# pip install requests==2.0.0
# pip uninstall requests

# 네이버 페이지의 내용을 받아와서 화면세 텍스트로 출력(print)하시오.

response = requests.get('https://movie.daum.net/main/')
# print(response.status_code)
# print(response.url)
# print(response.headers)
# print(response.text)

# print(response)

# 네이버 페이지 내에서 H2 태그 뽑기

# 처음 생각
search_str = "h2"
contents = response.text


for line in contents.splitlines(): # print(content) 넣어서 어느 부분에서 어떻게 나오는지 확인하기
    # print(line)
    if search_str in line: # 
        print(line.strip())



