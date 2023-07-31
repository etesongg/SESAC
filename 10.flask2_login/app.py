from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

"""
LoginManager: 로그인 관리를 담당하는 클래스로, Flask 애플리케이션에서 로그인 기능을 초기화하고 관리하는 역할을 합니다.
UserMixin: UserMixin 클래스는 Flask-Login이 기본적으로 사용하는 사용자 모델 클래스를 정의하기 위해 사용됩니다. 이 클래스를 사용하여 사용자 모델 클래스에 필요한 메서드들을 간단하게 추가할 수 있습니다.
login_user: 로그인 처리를 위해 사용되는 함수로, 인증이 성공적으로 완료된 사용자를 로그인 상태로 만듭니다. 이 함수를 호출하면 세션에 사용자 정보가 저장되어 사용자를 인증된 상태로 유지할 수 있습니다.
login_required: 데코레이터로, 특정 뷰 함수를 보호하는 데 사용됩니다. 이 데코레이터가 적용된 뷰 함수는 로그인된 사용자만 접근할 수 있으며, 로그인되지 않은 사용자는 로그인 페이지로 리디렉션됩니다.
logout_user: 로그아웃 처리를 위해 사용되는 함수로, 현재 로그인된 사용자를 로그아웃 상태로 만듭니다. 세션에서 사용자 정보를 삭제하여 인증을 끝내는 역할을 합니다.
current_user: 현재 로그인된 사용자를 나타내는 객체입니다. 로그인되지 않은 경우 AnonymousUserMixin 객체가 반환됩니다. 이를 통해 로그인된 사용자의 정보를 뷰 함수에서 간단하게 접근할 수 있습니다.
"""

app = Flask(__name__)

# 환경설정
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db 생성
db = SQLAlchemy(app)

# db 마이그레이션 모듈로딩
migrate = Migrate(app, db)

# 로그인 매니저 생성
login_manager = LoginManager(app)
login_manager.login_view = 'login' # 로그인 페이지 url을 명시해 주는 것


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # password_hash = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80))

    def set_password(self, password):
        self.password = password
        # self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return self.password == password
        # return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 로그인 기능 구현
    # 1. Form으로 부터 id/pw 받아온다
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # password_hash = md5(password)

    # 2. db로 부터 쿼리해서 ip/pw 맞는지 확인한다
        user = User.query.filter(User.username==username).first()
    # 3. 성공했으면 로그인정보를 저장하고, 로그인 한 페이지로 이동
    #    실패했으면 오류를 알려줌
        if user and user.check_password(password): 
            login_user(user)
            flash("Login에 성공하였습니다.", "success")
        else:
            flash("Login에 실패하였습니다.", "danger")

    return redirect(url_for('main'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout에 성공하였습니다.", "success")
    return redirect(url_for('main'))

@app.route('/profile_edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    # 프로필 수정 기능 구현
    # 1. 폼을 통해서 수정할 정보를 가져온다. (password를 받아온다)
    if request.method == 'POST': # main, profile_edit에서 profile_edit 할때 오는 post구분하기 위해 main에서 method를 get으로 변경함
        new_password = request.form['new_password']
        new_email = request.form['new_email']
        
    # 2. 저장할 장소(즉 현재 사용자)를 가져온다 (current_user 를 통해서 접근 가능)
    # 3. 받아온 정보를 db에 저장한다. 
        # user = User.query.filter_by(username=current_user.username).first()
        # user.password = new_password
        if new_password:
            current_user.set_password(new_password)
        if new_email:
            current_user.email = new_email
        
        db.session.commit()
        flash("프로필이 수정 되었습니다.", "success")
    
        return redirect(url_for('main'))
    
    return render_template('profile_edit.html')

# 신규 사용자 생성
@app.route('/register', methods=['GET', 'POST'])
def register():
    # 회원가입 폼을 만든다
    # 1. 회원가입 정보를 받아온다 (id/pw)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    # 2. 사용자가 있는지 조회
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("사용자가 이미 존재합니다.", "danger")
            return redirect(url_for('register'))
    # 3. db에 저장한다
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("회원가입에 성공하였습니다.", "primary")
        return redirect(url_for('main'))
    
    return render_template('register.html')


# 사용자 목록 조회
@app.route('/users')
@login_required
def view_users():
    # 있는 사용자 모두를 출력한다.
    # 1. 사용자 정보를 모두 조회한다.
    users = User.query.all()
    # 2. html 페이지에 조회한 정보를 전달해서 출력한다.
    return render_template('users.html', users=users)

# @app.route('/delete', methods=['POST'])
# def delete():
#     user = session['username']


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



