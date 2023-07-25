from flask import Flask, render_template, redirect, url_for
import csv


# 변수에 클래스 할당
app = Flask(__name__)

# 라우팅
@app.route('/')
# def root():
#     return redirect(url_for("home", name=""))

@app.route('/<name>')
def home():
    # user_names=["Alice", "Bob", "Charlie", "David", "Eve", "admin"]
    users = [
        # {'name':'Alice', 'age':25, 'phone':'123-456-7890'},
        # {'name':'Bob', 'age':30, 'phone':'987-654-3210'},
        # {'name':'Charlie', 'age':35, 'phone':'555-123-4567'}
    ]

    def load_file(txt_file_name):
        with open(txt_file_name, "r", encoding="UTF8") as file:
            lines = file.readlines()

        data = []
        for line in lines:
            data.append(line.strip())
        return data
    list(load_file('order.csv'))
    list(load_file('item.csv'))
    list(load_file('store.csv'))
    
    
    f = open('user.csv','r', encoding='UTF8')
    rdr = csv.DictReader(f)
    reponse = render_template("index.html", username = rdr)

    return reponse

    

# @app.route('/login')
# def login():
#     return render_template("login.html")

# 이 파일을 실행할때 어디서부터 시작할지 메인함수부터 시작
if __name__ == "__main__":
    app.run(debug=True)