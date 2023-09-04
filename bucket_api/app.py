import json
import os
import sys

from flask import Flask
from exhibition_kcisa import insert_exhibition_kcisa

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import DEBUG, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models.model import db

app = Flask(__name__)

app.instance_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'database')
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///today-exhibition3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.debug = DEBUG

db.init_app(app)

@app.route('/')
def main():
    insert_exhibition_kcisa()
    return "success"


if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run(port=8000)

def load_secrets():
    with open("./secrets.json", "r") as secrets_file:
        secrets = json.load(secrets_file)
    return secrets