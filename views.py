from application import get_app
from models import Company, get_db
from flask import render_template, request, flash
from wtforms import StringField
from flask_wtf import Form, FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired

app = get_app()
db = get_db()

class SearchForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired(),Length(max=4)],render_kw={"placeholder": "company symbol (1-4 letters)"})


@app.route('/', methods=["GET", "POST"])
def index():
    form = SearchForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            return render_template('index.html',module='home', companies = Company.query.all(), symbol=request.form["company"], form = form)
        flash("The ticker must have between 1 and 4 letters")
    return render_template('index.html',module='home', companies = Company.query.all(), form = form)

