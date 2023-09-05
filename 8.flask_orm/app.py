from flask import Flask, render_template, request
from flask import redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=1)

app.secret_key = "this_is_my_secrey_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 테이블 이름은 소문자로 변환하고 이를 테이블 이름으로 사용하여 클래스 이름에서 파생되거나
# 내부에 __tablename__ = 'users' 로 지정할 수 있다.

# Python 클래스 내부에서 _id라는 이름으로 열(Column)을 정의
# but "id"를 통해 데이터베이스에서 이 열의 이름은 "id"로 지정
# 즉, 데이터베이스에서는 "id"라는 이름으로 해당 열을 저장
class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
   
users = {
    'user1': {'password': 'password123'},
    'user2': {'password': 'abc123'}
}

@app.route('/')
def home():
    username = None
    if 'username' in session:
        username = session['username']
        flash("Login에 성공하였습니다.")
    
    return render_template('index.html', username=username )

@app.route('/view')
def view():
    return render_template('view.html', users=Users.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 데이터 조회
        found_user = Users.query.filter_by(name=username).first()
        if found_user:
            flash("Login Successful")

        else:
            # 데이터베이스에 데이터 추가
            user = Users(username, password, "")
            db.session.add(user)
            db.session.commit()
            flash("User Created")
            
        session['username'] = username
        return redirect(url_for('home'))
        
    return render_template('login.html')

@app.route('/delete', methods = ['POST'])
def delete():
    user = session['username']
    
    if request.method == 'POST':
        action = request.form["action"]
        if action == "DELETE":
            # 데이터베이스에 데이터 삭제
            Users.query.filter_by(name=user).delete()
            db.session.commit()
            return redirect(url_for('logout'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # db 초기화?생성?
    with app.app_context():
        db.create_all()
    app.run(debug=True)


