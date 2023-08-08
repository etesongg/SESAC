from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('movie_data.db', check_same_thread=False)
cur = conn.cursor()

@app.route('/')
def index():
    cur.execute('''
                select * from movies
                ''')
    
    result = cur.fetchall()

    return render_template('index.html',result=result )

if __name__ == '__main__':
    app.run(debug=True)
