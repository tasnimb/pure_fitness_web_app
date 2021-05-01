from flask import Flask, redirect, url_for
from application import app, db, login_manager
from datetime import date
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False,unique=False)
    last_name = db.Column(db.String(30), nullable=False,unique=False)
    email = db.Column(db.String(40),unique=True,nullable=False)
    date_of_birth=db.Column(db.Date,nullable=True)
    phone_number = db.Column(db.String(15))
    address = db.Column(db.String(70))
    postcode = db.Column(db.String(8))
    city = db.Column(db.String(20))
    password = db.Column(db.String(200),primary_key=False, unique=False,nullable=False)


class Activity(db.Model):
    __tablename__ = 'Activity'
    activity_type_id = db.Column(db.Integer, primary_key=True)
    activity_type = db.Column(db.String(30), nullable=False, unique=True)
    activity_description = db.Column(db.String(200), nullable=False, unique=True)
    duration = db.Column(db.String(200), nullable=False)
    instructor_name = db.Column(db.String(30), nullable=False)


class ActivityBooked(db.Model):
    __tablename__ = 'BookActivity'
    booking_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50))
    date = db.Column(db.Date, nullable=False)
    activity_type = db.Column(db.String(15), nullable=False)
    timeslot = db.Column(db.String(15), nullable=False)


class Faq(db.Model):
    __tablename__ = 'Faq'
    faq_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email_address = db.Column(db.String(50))
    subject = db.Column(db.String(100), nullable=False)
    question = db.Column(db.String(500), nullable=False)

