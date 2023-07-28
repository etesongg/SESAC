from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'abcd1234' # 세션 암호화를 위한 나만의 키

# 상품 정보 등록
items = {
    'item1': {'name': '상품1', 'price': 1000 },
    'item2': {'name': '상품2', 'price': 2000 },
    'item3': {'name': '상품3', 'price': 3000 }
}

@app.route('/')
def index():
    return render_template('index.html', items = items)

@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    if 'cart' not in session: # 세션에 cart가 없으면 
        session['cart'] = {} # 초기화
    
    # 카트에 물건 담기
    if item_name in session['cart']: # 세션에 있니? 있으면 담고 
        session['cart'][item_name] += 1
    else:
        session['cart'][item_name] = 1

    # 세션 데이터가 수정되었음을 flask에 알림
    session.modified = True # db 사용하면 쓸 필요x

    # 담은 이후 액션
    return redirect(url_for('index'))

# 미션1. index.html 페이지에서, 상품명을 클릭해서 이 url이 호출되도록 구현하시오.
# 미션2. 장바구니 보기 버튼(링크) 추가
# 미션3. 장바구니 내용 세션을 통해 가져와서 cart.html에 출력
#   3-1. 상품명 : 개수 출력
#   3-1. 상품명 : 개수 : 개별단가(unit_price) 출력(가격은 내부 db를 통해서 가져옴)
#   3-3 상품명 : 개수 : 가격(상품명x개수) 계산해서 출력
#   3-4 여러개의 상품명과 가격의 합산인 total 출력하기 

@app.route('/view_cart')
def view_cart():
    # 세션에서 카트 정보를 가져와서 출력한다.
    cart_items = {}
    cart_items = session.get('cart')
    total = 0
    
    for item_name, quantity in session.get('cart', {}).items():
        item = items.get(item_name)
        if item:
            cart_items[item_name] = {'name': item['name'], 'quantity': quantity, 'price': item['price'], 'unit_price': (quantity*item['price'])}
            total += (quantity*item['price'])
    print(cart_items)
    print(total)
    return render_template('cart.html', cart_items=cart_items, total=total)


@app.route('/remove_item_from_cart/<item_name>')
def remove_item_from_cart(item_name):
    # 상품 삭제
    session['cart'].pop(item_name)

    # 세션 데이터가 수정되었음을 flask에 알림???
    session.modified = True
    return redirect(url_for('view_cart'))

# @app.route('/delete')
# def delete():
#     session.pop('name')
#     redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)