from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # 테이블로 2023-1...2023-12까지 월간 매출액 구하는 쿼리
    # 1. db 접속
    conn = sqlite3.connect('crm.db')

    # 2.커서 만들기
    cursor = conn.cursor()
    # 3. sql 구문 작성
    query = """
    SELECT SUBSTR(o.ordered_at, 1, 7) AS YearMonth, SUM(i.unit_price) AS MonthlyRevenue
    FROM "order" o
    JOIN order_item oi ON o.id = oi.order_id
    JOIN item i ON oi.item_id = i.id
    GROUP BY YearMonth
    """
    # 4. 쿼리문을 실행해서 결과를 받아온다.(리스트 형태)
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    
    # 5. 랜더템플릿에 데이터를 전송한다.
    labels = []
    values = []

    for row in rows:
        lable, value = row
        labels.append(lable)
        values.append(value)
    
    return render_template("index.html", rows=rows, labels=labels, values=values)

if __name__ == "__main__":
    app.run(debug=True)