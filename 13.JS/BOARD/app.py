from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)
db = Database()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['post'])
def create():
    title = request.form['title']
    message = request.form['message']

    sql = 'insert into board(title, message) values("{}","{}")'.format(title, message)
    db.execute(sql)
    db.commit()
    return "OK"

@app.route('/list', methods=['get'])
def list():
    sql = "select * from board"
    result = db.execute_fetch(sql)
    
    # json 형태로 만들어 주기 dict(), zip()
    tuple_keys = ('id', 'title','message')
    dict_list = []
    for r in result:
        dict_value = dict(zip(tuple_keys, r))
        dict_list.append(dict_value)

    return dict_list

@app.route('/delete', methods=['post'])
def delete():
    id = request.form['id']
    print(id)
    sql = 'delete from board where id = "{}"'.format(id)
    db.execute(sql)
    db.commit()
    return "OK"


@app.route('/modify', methods=['post'])
def modify():
    id = request.form['id']
    title = request.form['title']
    message = request.form['message']
    print(id, title, message)
    sql = 'update board set title=?, message=? where id=?'
    db.execute(sql, (title, message, id))
    db.commit()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)