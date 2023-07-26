from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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

    def __repr__(self):
        return f'<Store {self.ordered_at}, {self.store_id}, {self.user_id}>'
    



@app.route('/')
def home():
    # users = User.query.filter_by(name="강은지").all()
    # print(users)
    # stores = Store.query.all()
    # print(stores)
    # orders = Order.query.all()
    # for o in orders:
    #     print(o)
    # # user = User.query.filter_by(name="장예진").first()
    # # order_by_user = user.orderR
    # # print(order_by_user)

    # # 1. 장예진이 방문한 성점명들을 출력하시오.
    # # 1-1. sql 쿼리문 적어보기
    # # select u.name, s.name
    # # from user u
    # # join orders o on u.id = o.userId
    # # join store s on o.storeId = s.id
    # # where u.name='장예진'

    # # 1-2. sql 쿼리문을 SQLAlchemy 문법으로 작성
    # users_order_stores = db.session.query(User, Order, Store) \
    #     .join(Order, User.id == Order.user_id) \
    #     .join(Store, Store.id == Order.store_id) \
    #     .filter(User.name == "정지유").all()
    
    # for user, order, store in users_order_stores:
    #     print(f'{user.name}님이 방문한 상점은 {store.name}, 시간은 {order.ordered_at}')
 

    users = User.query.filter_by(name="정지유").first() # 여기 all()로 하면 안 됨
    # 여기에서 "장예진"이 주문한 주문내역
    if users:
        order_by_user = users.orderR
        for order in order_by_user:
            store = order.store
            print(f'정지유님이 방문한 상점은 {store.name} 시간은 {order.ordered_at}')
    else:
        print('None found')


    return "Hello"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)


