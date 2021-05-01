from flask import Flask
from application import app, db
from datetime import date


class CustomerContact(db.Model):
    __tablename__ = 'CustomerContact'
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    date_of_birth=db.Column(db.Date,nullable=True)
    phone_number = db.Column(db.String(15))
    address_line = db.Column(db.String(70))
    postcode = db.Column(db.String(8))
    city = db.Column(db.String(20))


class CustomerLogin(db.Model):
    __tablename__ = 'CustomerLogin'
    customerlogin_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50))
    password = db.Column(db.String(200))


class Activity(db.Model):
    __tablename__ = 'Activity'
    activity_type_id = db.Column(db.Integer, primary_key=True)
    activity_type = db.Column(db.String(30), nullable=False, unique=True)
    activity_description = db.Column(db.String(200), nullable=False, unique=True)
    duration = db.Column(db.String(200), nullable=False)
    instructor_name = db.Column(db.String(30), nullable=False)


class ActivityBooked(db.Model):
    __tablename__ = 'ActivityBooked'
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
