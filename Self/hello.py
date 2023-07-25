from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>hello sesac from flask</h2>
    <P>welcome to flask</p>
    <div>안냥</div>
    <p><a href="/user">user's homepage</a></p>
    """

@app.route("/user")
def user_none():
    return """
    <ul>
    <li><a href="/user/tom">tom</a> </li>
    <li><a href="/user/john">john</a> </li>
    <li><a href="/user/bill">bill</a> </li>
    </ul>
    """

@app.route("/user/<name>")
def user(name):
    return f"""<h1>This is {name}'s homepage<h1>
    <p><a href="/">welcome to flask</a> </p>
    <p><a href="/user">user's list</a> </p>
    """

@app.route('/admin')
def admin():
    # if user is not loggedin:
    #     redirect 해서 login 페이지로 전달
    return redirect(url_for('user', name="admin"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)