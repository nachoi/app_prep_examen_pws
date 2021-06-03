from application import get_app
from models import Company, get_db
from flask import render_template, request
from wtforms import StringField, Form
from wtforms.validators import InputRequired, Length

app = get_app()
db = get_db()

class SearchForm(Form):
    company = StringField('Company', validators=[InputRequired(),Length(min=1,max=4)],render_kw={"placeholder": "company symbol (1-4 letters)"})

@app.route('/', methods=["GET", "POST"])
def index():
    form = SearchForm(request.form)
    if request.method == "GET":
        return render_template('index.html',module='home', companies = Company.query.all(), form = form)
    return render_template('index.html',module='home', companies = Company.query.all(), symbol=request.form["company"], form = form)
