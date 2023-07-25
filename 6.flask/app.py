from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import session
from flask import flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/', methods=["GET", "POST"])
def home():
    name = None
    age = None
    flash("메시지 테스트")
    if request.method == 'GET':
        name = request.args.get('name')
        age = request.args.get('age')
    elif request.method == 'POST':
        name = request.form["name"]
        session['userid'] = name
        # session.permanent = True
        flash("Login에 성공하였습니다.")
        flash("메시지 플래슁 예제입니다.")
    else:
        return "UNKNOWN METHOD"

    return render_template("index.html", name = name, age = age)

@app.route('/user')
def user():
    if "userid" in session:
        user = session['userid']
        return f'<h1>Hello, {user}'
    else:
        return redirect(url_for('home'))

@app.route('/redirect')
def redirect_example():
    # return redirect('/')
    return redirect(url_for('user'))

if __name__ == '__main__':
    app.run(debug=True)