import sqlite3
import hashlib

# db에 접속
conn = sqlite3.connect('hello.db')

# conn을 통해서 메시지를 주고 받음
# 로우레벨 접속을 한 소켓 인터페이스
# 커서(명렁어를 주고 받는 위치)
c = conn.cursor()

# 미션 1.
# 사용자 콘솔로부터 username/password를 받아서 쿼리해서 동작하는 함수를 구현하시오
def login(username, password):
    c.execute("select * from users where username=? and password=?",(username, password))
    result = c.fetchall()
    if len(result) == 1:
        print("로그인에 성공하였습니다")
    else:
        print("로그인에 실패하였습니다.")
    
# username = input("사용자 이름을 입력하세요: ")
# password = input("비밀번호를 입력하세요: ")
# login(username, password)

# 미션 2.
# 암호화 (단방향 암호화인 hash) 처리해서 로그인 하는 코드 구현하기 (hashlib 사용하기)
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def cleanup_table():
    c.execute("drop table if exists users2")
    c.execute("""create table users2
                (id integer primary key autoincrement,
                username text,
                password text)""")
    conn.commit()

def insert_user():
    users = [
        ('user1', 'abcd1111'),
        ('user2', 'abcd2222'),
        ('user3', 'abcd3333'),
        ('user4', 'abcd4444'),
        ('user5', 'abcd5555'),
    ]
    
    for u in users:
        c.execute("insert into users2(username, password) values(?,?)", (u[0], hash_password(u[1])))
        conn.commit()

# cleanup_table()
# insert_user()


# 미션 2-1.
# 수동으로 username, password => username, 해쉬된 password로 hashlib를 사용해서 저장하기
# 미션 2-2.
# 이걸로 조회하기

def login2(username, password):
    input_password = hash_password(password)
    c.execute("select * from users2 where username=? and password=?", (username, input_password))
    user = c.fetchone()

    if user is None:
        print("로그인 실패 (사용자 없음)")
    else:
        print("로그인 성공")
        

username = input("사용자 이름을 입력하세요: ")
password = input("비밀번호를 입력하세요: ")
login2(username, password)

