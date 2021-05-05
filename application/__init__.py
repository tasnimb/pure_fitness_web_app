from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:password@localhost/pure_fitness"


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SESSION_TYPE'] = 'sqlalchemy'



db = SQLAlchemy(app)
login_manager=LoginManager(app)

app.config['SESSION_SQLALCHEMY'] = 'db'


