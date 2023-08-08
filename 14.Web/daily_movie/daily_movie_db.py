import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import date

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

# 데이터베이스 설정
conn = sqlite3.connect('daily_movie_data.db')
cur = conn.cursor()

# 테이블 생성 
# 고정된 값과 가변하는 값을 구분해서 테이블 만들기
cur.execute('''
            create table if not exists movies (
            id integer primary key autoincrement,
            title text,
            poster_url text,
            short_description text,
            img text)
            ''')

cur.execute('''
            create table if not exists daily_info (
            id integer primary key autoincrement,
            movie_id integer,
            date text,
            rating text,
            reservation_rate text,
            rank text,
            foreign key(movie_id) references movies (id)
            )
            ''')

# 다음영화랭킹(제목/평점/예매율)

movies = soup.select('#mainContent > div > div.box_ranking > ol > li')

for movie in movies:
    title_tag = movie.select_one('div > div.thumb_cont > strong')
    grade_tag = movie.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(1) > span')
    num_tag = movie.select_one('div.thumb_cont > span.txt_append > span:nth-child(2) > span')
    link = movie.select_one('div > div.thumb_item > div.poster_info > a')
    rank = movie.select_one('div.thumb_item > div.poster_movie > span.rank_num')
    img_tag = movie.select_one('div.thumb_item > div.poster_movie ')
    if title_tag:
        movie_title = title_tag.text.strip()
        movie_grade = grade_tag.text.strip()
        movie_num = num_tag.text.strip().replace('%','')
        movie_url = 'https://movie.daum.net/' + link['href']
        movie_short = link.text.strip()
        rank = rank.text.strip()
        img = img_tag.img["src"]

        # 데이터 삽입
        cur.execute('insert into movies (title, poster_url, short_description, img) values (?,?,?,?)', (movie_title, movie_url, movie_short, img))
        conn.commit()

        cur.execute('select id from movies where title=?',(movie_title,))
        movie_id = cur.fetchone()[0]
        fetch_date = date.today()

        cur.execute('insert into daily_info (movie_id, date, rating, reservation_rate, rank) values (?,?,?,?,?)', (movie_id, fetch_date, movie_grade, movie_num, rank ))

        conn.commit()
