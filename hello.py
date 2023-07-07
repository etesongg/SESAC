import sqlite3

# db에 접속
conn = sqlite3.connect('hello.db')

# conn을 통해서 메시지를 주고 받음
# 로우레벨 접속을 한 소켓 인터페이스
# 커서(명렁어를 주고 받는 위치)
c = conn.cursor()

user_input = "user1"
pass_input = "abcd1111"
c.execute("SELECT * FROM users WHERE username=? and password=?", (user_input, pass_input))
result = c.fetchall()
for r in result:
    print(r)

# 로그인 코드를 구현한다.
if len(result) == 1:
    print("로그인에 성공하였습니다.")
else:
    print("로그인에 실패하였습니다.")

# db 사용이 다 끝났을때, 변경사항들을 최종 기록
conn.commit()

# 접속을 종료
conn.close()

