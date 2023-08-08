from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('daily_movie_data.db', check_same_thread=False)
cur = conn.cursor()

@app.route('/')
def index():
    cur.execute('''
                select distinct date from daily_info
                order by date desc 
                ''')
    result = cur.fetchall()

    return render_template('index.html', result=result)

@app.route('/daily_movie/<date>')
def daily_movie(date):
    cur.execute('''
                select daily_info.rank, movies.title, daily_info.rating, daily_info.reservation_rate, movies.short_description, movies.img, movies.poster_url 
                from movies 
                join daily_info on movies.id = daily_info.movie_id
                where daily_info.date = ?
                ''', (date,))
    result = cur.fetchall()

    cur.execute('''
                select distinct date from daily_info
                order by date desc 
                ''')
    date_result = cur.fetchall()

    return render_template('daily_movie_v2.html', result=result, date=date, date_result=date_result)

if __name__ == '__main__':
    # cur.execute('''
    #                 SELECT * 
    #                 FROM daily_info
    #                 LIMIT 20
    #             ''')
    # result = cur.fetchall()
    # result2 = []
    # for r in result :
    #     r = list(r)
    #     r = r[1:]
    #     r[1] = '2023-08-11'
    #     r = tuple(r)
    #     result2.append(r)
    
    # for r in result2 :
    #     cur.execute('''INSERT INTO daily_info(movie_id, date,   rating,
    #         reservation_rate, rank)
    #             VALUES(?, ?, ?, ?, ?)
    #         ''', r)
    #     conn.commit()

    # # 추가로 들어간 데이터 삭제하기 
    # for i in range(61, 81) : # 실행하기 전에 범위 수정하기
    #     sql ="""
    #     DELETE FROM daily_info WHERE id = ?
    # """
    #     cur.execute(sql, (i,))
    #     conn.commit()
    app.run(debug=True)
    
