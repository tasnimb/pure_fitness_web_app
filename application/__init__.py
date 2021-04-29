from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_change_password import ChangePassword, ChangePasswordForm, SetPasswordForm
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:Thamside6896@localhost/pure_fitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

flask_change_password = ChangePassword(min_password_length=1)
flask_change_password.init_app(app)

app.permanent_session_lifetime = timedelta(minutes=2)


db = SQLAlchemy(app)
