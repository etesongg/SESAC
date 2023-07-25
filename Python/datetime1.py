import datetime

# 각 모듈별 사용법은 그 원자자들이 메뉴얼을 만들어 두었음
# 개별 모듈이면 원자의 홈페이지 (또는 패키지 다운로드 받은 공식 사이트)를 통해서 참조
# not todo : 네이버 블로그의 남의 글 참조하기
# todo : 원문을 참조해야함

# https://docs.python.org/

current_time = datetime.datetime.now()
print("현재시간: " , current_time)

specific_time = datetime.datetime(2023,6,20,10,30,00)
print("내가 만든 날짜 : ", specific_time)
