from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import init_app
app = init_app(__name__)

app.config['SECRET_KEY'] = 'EstoDeflask_wtfEsLaPolla!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/yahoo_ticker_sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import init_db
db = init_db(app)

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

#import sqlite3
#conn = sqlite3.connect("./database/yahoo_ticker_sample.db")

#import pandas as pd
#df = pd.read_sql("SELECT * FROM yahoo_ticker_sample;", conn)

import views

if __name__ == '__main__':
    manager.run()