from flask_sqlalchemy import SQLAlchemy

db = None

def init_db(app):
    global db
    if db == None:
       db = SQLAlchemy(app) # class db extends app
    return db

def get_db():
    global db
    if db == None:
        from application import get_app
        app = get_app()
        db = init_db(app)
    return db

from application import get_app
app = get_app()
db = init_db(app)

class Company(db.Model):
    __tablename__ = 'yahoo_ticker_sample'
    index = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.Text)
    country = db.Column(db.Text)
    sector = db.Column(db.Text)
    RefIndex = db.Column(db.Text)

