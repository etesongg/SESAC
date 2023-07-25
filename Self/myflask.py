from flask import Flask
import random

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "welcome"

@app.route("/create/")
def create():
    return "create"

# @app.route("/read/1/")
# def read():
#     return "read 1"

# 가변적인 변수를 라우트가 받기 위해선 어떻게 해야 할까?
# @app.route("read/< 변수 >/")를 통해 해결할 수 있다

# < 변수 > 를 정하면 그것을 받는 함수의 파라미터 중에 같은 이름의 파라미터가 그 값을 받을 수 있게 해준다 <id> 넣고 read(name) 이러면 TypeError 발생

# @app.route("/read/<id>/")
# def read1(id):
#     print(id)
#     return "read " + id

# 순서가 있는 데이터는 list에 담기 좋음
# 항목에 대한 제목, id, 클릭했을때 본문에 나타날 내용이 있다면 딕셔너리에 담기 좋음

topics = [
    {"id": 1, "title":"html", "body":"html is ..."},
    {"id": 2, "title":"css", "body":"css is ..."},
    {"id": 3, "title":"javascript", "body":"javascript is ..."}
]
# 일반 적인 웹 프레임 워크에서 데이터는 데이터 베이스에 저장하니 나중에는 topics = 데이터 읽어오는 코드로 바꿔주면 동일하게 사용할 수 있음 

# 다 구현 후 중복되는 코드 정리

def template(contents, content):
    return f'''<!doctype html>
    <html>
        <head>
        <title>Flask 기초</title>
        </head>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''

def getContents():
    litags = " "
    for topic in topics:
        litags = litags + f"<li><a href='/read/{topic['id']}/'>{topic['title']}</a></li>"
    return litags

@app.route("/")
def index():
    return template(getContents(), "<h2>Welcome</h2>Hello, Web")

# <ol>
#     <li><a href="/read/1/">html</li>
#     <li><a href="/read/2/">css</li>
#     <li><a href="/read/3/">javascrip</li>
# </ol>
# -> litags

# litags = litags + f"<li><a href='/read/{topic['id']}/'>{topic['title']}</a></li>"
# "" '' 잘 구분해서 사용하기, 링크 마지막에 / 쓰기
# a 닫는 태그 잘 하기


# 주의 
# IndentationError: unindent does not match any outer indentation level 들여쓰기 오류 주의

@app.route("/read/<int:id>/")
def read(id):
    title = " "
    body = " "
    for topic in topics:
        if id == topic["id"]: # 하지만<id>로 들어오는 값의 타입은 문자열임, 비교할 수 없으니 id값을 int로 지정해줌 <int:id>/
            title = topic["title"]
            body = topic["body"]
    return template(getContents(), f"<h2>{title}</h2>{body}")


# <h2>Welcome</h2>  ->  {title}
# hello, web  ->  {body}






if __name__ == "__main__":
    app.run(debug=True)