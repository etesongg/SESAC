import requests
from bs4 import BeautifulSoup
import sqlite3 

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

# 데이터베이스 설정
conn = sqlite3.connect('movie_data.db')
cur = conn.cursor()

# 테이블 생성 
cur.execute('''
            create table if not exists movies (
            id integer primary key autoincrement,
            title text,
            rating text,
            reservation_rate text,
            poster_url text,
            short_description text)
            ''')

# 다음영화랭킹(제목/평점/예매율)

movies = soup.select('#mainContent > div > div.box_ranking > ol > li')

for movie in movies:
    title_tag = movie.select_one('div > div.thumb_cont > strong')
    grade_tag = movie.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(1) > span')
    num_tag = movie.select_one('div.thumb_cont > span.txt_append > span:nth-child(2) > span')
    link = movie.select_one('div > div.thumb_item > div.poster_info > a')
    if title_tag:
        movie_title = title_tag.text.strip()
        movie_grade = grade_tag.text.strip()
        movie_num = num_tag.text.strip().replace('%','')
        movie_url = 'https://movie.daum.net/' + link['href']
        movie_short = link.text.strip()
        
        # 데이터 삽입
        cur.execute('insert into movies (title, rating, reservation_rate, poster_url, short_description) values (?,?,?,?,?)',(movie_title, movie_grade, movie_num, movie_url, movie_short))

        conn.commit()

    