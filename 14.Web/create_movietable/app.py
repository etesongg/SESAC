from flask import Flask, render_template, request
from database import Database

from daum_movie import get_daum_movie

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    movie_datas = get_daum_movie('movie_rank')
    
    for movie_data in movie_datas:
        title = movie_data['movie_title']
        # grade = movie_data['movie_grade']
        # sales_rate = movie_data['movie_num']
        # print(title, grade, sales_rate)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)