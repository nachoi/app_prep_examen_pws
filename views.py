from application import get_app
from models import Company, get_db
from flask import render_template, request, flash
from wtforms import SelectField
from flask_wtf import Form, FlaskForm
from wtforms.validators import Length

app = get_app()
db = get_db()


class SelectForm(FlaskForm):
    company = SelectField('Company', validators=[Length(min=1,max=4)], choices=[('', 'Select an option')])


@app.route('/', methods=["GET", "POST"])
def index():
    form = SelectForm()
    companies = Company.query.all()
    companies_list=[(i.ticker, i.ticker) for i in companies]
    form.company.choices += companies_list
    if request.method == 'POST':
        if form.validate_on_submit():
            return render_template('index.html',module='home', companies = Company.query.all(), symbol=request.form["company"], form = form)
        else:
            flash("The ticker must have between 1 and 4 letters")
    return render_template('index.html',module='home', companies = companies, form = form)

