from flask import Flask
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Tuntun123@@@db/main"

CORS(app)

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True,autoincrement = False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    user_id = db.Column(db.Integer, primary_key =True)
    product_id = db.Column(db.Integer, primary_key =True)

    UniqueConstraint('user_id', 'product_id', name = 'user_product_unique')

@app.route("/")
def index():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
