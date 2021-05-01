from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_session import Session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:Thamside6896@localhost/pure_fitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SESSION_TYPE'] = 'sqlalchemy'


app.permanent_session_lifetime = timedelta(minutes=2)

db = SQLAlchemy(app)

app.config['SESSION_SQLALCHEMY'] = 'db'

# sesh = Session(app)
