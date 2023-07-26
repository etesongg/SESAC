from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import os

app = Flask(__name__)

app.instance_path = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HugeCrm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    # 컬럼 셋업
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))
    # 관계 (relation) 셋업
    orderR = db.relationship('Order', backref='user')

    # 내가 원하는 형태
    def __repr__(self):
        return f'<User {self.name}, {self.gender}, {self.age}>'
    
class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    address = db.Column(db.String(64))
    orderR = db.relationship('Order', backref='store')

    # print를 편하게 도와주는 선택사항임(이거 안 하면 id 값만 나옴) 
    def __repr__(self):
        return f'<Store {self.name}, {self.type}, {self.address}>'

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.String(64), primary_key=True)
    ordered_at = db.Column(db.String(64))
    store_id = db.Column(db.String(64), db.ForeignKey('store.id'))
    user_id = db.Column(db.String(64), db.ForeignKey('user.id'))
    order_itemR = db.relationship('Order_Item', backref = 'order')

    def __repr__(self):
        return f'<Order {self.ordered_at}, {self.store_id}, {self.user_id}>'
    
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    unit_price = db.Column(db.Integer())
    order_itemR = db.relationship('Order_Item', backref = 'item')

class Order_Item(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(db.String(64), primary_key=True)
    order_id = db.Column(db.String(64), db.ForeignKey('order.id'))
    item_id = db.Column(db.String(64), db.ForeignKey('item.id'))



@app.route('/')
def home():
    # 1. 정지유님이 방문한 성점명들을 출력하시오.
    # 1-1. sql 쿼리문 적어보기
    # select u.name, s.name
    # from user u
    # join orders o on u.id = o.userId
    # join store s on o.storeId = s.id
    # where u.name='장예진'

    # # 1-2. sql 쿼리문을 SQLAlchemy 문법으로 작성
    # 1) join 사용
    # users_order_stores = db.session.query(User, Order, Store) \
    #     .join(Order, User.id == Order.user_id) \
    #     .join(Store, Store.id == Order.store_id) \
    #     .filter(User.name == "정지유").all()
    
    # for user, order, store in users_order_stores:
    #     print(f'{user.name}님이 방문한 상점은 {store.name}, 시간은 {order.ordered_at}')
 
    # 2) relationship 사용
    # users = User.query.filter_by(name="정지유").first() # 여기 all()로 하면 안 됨
    
    # if users:
    #     order_by_user = users.orderR
    #     # order_by_user = [<Order 2023-06-03 12:57:12, 568f8334-d99f-46c6-9aec-ce79a5ab3e5e, 9afd612f-ee32-4768-93c9-57ceb2e7d964>, <Order 2023-09-07 15:5...
    #     for order in order_by_user:
    #         store = order.store
    #         # store = [<Store 스타벅스 강서13호점, 스타벅스, 광주 동구 2길 2>, <Store 투썸 신촌7호점, 투썸, 대전 남구 94로 94>...
    #         print(f'정지유님이 방문한 상점은 {store.name} 시간은 {order.ordered_at}')
    # else:
    #     print('None found')

    # --------------------------

    # # user의 성별이 male인 사람이 몇명인지 구하기(like, count 필요)
    # user_male_count = User.query.filter(User.gender.like('male')).count()
    # print(user_male_count)

    # # user의 이름에 '김'이 포함 되며 성별이 female인 사람의 {이름, 성별, 생일} 출력하기 (like, and 필요)
    # search_users = User.query.filter(User.name.like('%김%'), User.gender.like('female')).all()
    # for user in search_users:
    #     print(f'{user.name}, {user.gender}, {user.birthdate}')

    # 특정 유저의 주문 정보
    users = User.query.filter_by(id='94eab4b2-ed41-4c06-ad7c-d225314944b4').first()

    if users:
        order_by_user = users.orderR
        for order in order_by_user:
            # store = order.store # 출력되는 것 중에 store.~가 없으니 사용x
            print(f'{users.name}님의 주문 정보는 {order.id}, {order.ordered_at}, {order.store_id}')
    # order.ordered_at 기준으로 정렬하고 싶다면 from sqlalchemy import desc
    # order_by_user = sorted(users.orderR, key=lambda order: order.ordered_at, reverse=True)


    return "Hello"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)


