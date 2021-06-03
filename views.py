from application import get_app
from models import Company, get_db
from flask import render_template

app = get_app()
db = get_db()

@app.route('/')
def index():
    return render_template('index.html',module='home', companies = Company.query.all())