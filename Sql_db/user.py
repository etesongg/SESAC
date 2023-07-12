import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# 사용자 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT)''')

# 몇 명의 사용자 추가
users = [
    ('John Doe', 25, 'Male'),
    ('Jane Smith', 30, 'Female'),
    ('Michael Johnson', 35, 'Male'),
    ('Emily Davis', 28, 'Female'),
    ('David Lee', 32, 'Male'),
    ('Emma Wilson', 27, 'Female'),
    ('Daniel Brown', 31, 'Male'),
    ('Olivia Taylor', 29, 'Female'),
    ('Sophia Anderson', 33, 'Female'),
    ('Matthew Martin', 26, 'Male')
]

# cursor.executemany('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', users)

# 변경사항 저장
conn.commit()

# ------------------------

# 미션1. 성별 여자인 사람 출력
cursor.execute("select * from users where gender='Female'")
result = cursor.fetchall()
print("여자 고객 목록 :")
for r in result:    
    print(r)
print("-------------------")
# 미션2. 30살 이상인 사람만 출력
cursor.execute("select * from users where age >= 30")
result = cursor.fetchall()
print("나이가 30 이상인 고객 목록 :")
for r in result:  
    print(r)
print("-------------------")

# 미션3. 나이가 25 이상 30 이하인 사람 출력
cursor.execute("select * from users where age >= 25 and age <=30") # age between 25 and 30(25,30 포함)
print("나이가 25 이상 30 이하인 고객 목록 :")
result = cursor.fetchall()
for r in result:  
    print(r)
print("-------------------")

# 미션4. 성별로 그룹핑 (남/여 각각) 몇명인지 출력
cursor.execute("select gender, count(*) from users group by gender")
print("남/여 고객 수 :")
genders = cursor.fetchall()
for gender, count in genders:
    print(f"성별: {gender}: {count}")
print("-------------------")

# 미션5. John Doe의 나이를 25살 -> 26살로 업데이트 하시오
cursor.execute("update users set age=26 where name='John Doe'")
conn.commit() # 업데이트는 최종반영을 해줘야 db에서 바뀌는거임

cursor.execute("select * from users where name='John Doe'")
result = cursor.fetchall()
print(result)

# 미션6. Emily Davis 사용자를 삭제 하시오
cursor.execute("delete from users where name='Emily Davis'")
cursor.execute("select * from users where name='Emily Davis'")
result = cursor.fetchall()
print(result)