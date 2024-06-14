from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/markets")
def markets():
    items =[
        {"ID": 1, "name": "phone", "price": 10},
        {"ID": 2, "name": "monitor", "price": 20},
        {"ID": 3, "name": "computer", "price": 30},

    ]

    return render_template("markets.html", items=items)

