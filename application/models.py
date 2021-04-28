from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

from application import app, db
from sqlalchemy.orm import relationship


class CustomerName(db.Model):
    __tablename__ = 'Customer Name'
    customer_name_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    # contact=db.relationship('CustomerContact')


class CustomerContact(db.Model):
    __tablename__ = 'Customer Contact'
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name_id = db.Column(db.Integer, db.ForeignKey('Customer Name.customer_name_id'))
    phone_number = db.Column(db.String(15))
    email_address = db.Column(db.String(50), unique=True)
    address_line = db.Column(db.String(70))
    postcode_id = db.Column(db.Integer, db.ForeignKey('Postcode.postcode_id'))
    city_id = db.Column(db.Integer, db.ForeignKey('City.city_id'))
    # customername = db.relationship("CustomerName", back_populates="customer contact")


class City(db.Model):
    __tablename__ = 'City'
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(20))


class Postcode(db.Model):
    __tablename__ = 'Postcode'
    postcode_id = db.Column(db.Integer, primary_key=True)
    postcode = db.Column(db.String(8))


class CustomerLogin(db.Model):
    __tablename__ = 'Customer Login'
    customerlogin_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50))
    password = db.Column(db.String)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Activity(db.Model):
    __tablename__ = 'Activity'
    activity_type_id = db.Column(db.Integer, primary_key=True)
    activity_type = db.Column(db.String(30), nullable=False, unique=True)
    activity_description = db.Column(db.String(200), nullable=False, unique=True)
    duration = db.Column(db.String(200), nullable=False)
    instructor_name = db.Column(db.String(30), nullable=False)


class ActivityTime(db.Model):
    __tablename__ = 'ActivityTime'
    time_id = db.Column(db.Integer, primary_key=True)
    activity_time = db.Column(db.String(15), nullable=False)


class ActivityTimeslot(db.Model):
    __tablename__ = 'ActivityTimeslot'
    timeslot_id = db.Column(db.Integer, primary_key=True)
    activity_timeslot = db.Column(db.String(15), nullable=False)
    day_time_id = db.Column(db.Integer, db.ForeignKey('ActivityTime.time_id'))

    # def __init__(self, activity_timeslot):
    #     self.activity_timeslot = timeslot


class ActivityBooking(db.Model):
    __tablename__ = 'ActivityBooking'
    booking_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50), unique=True)
    date = db.Column(db.String(15), nullable=False)
    activity_type_id_b = db.Column(db.Integer, db.ForeignKey('Activity.activity_type_id'), nullable=False)
    time_id_b = db.Column(db.Integer, db.ForeignKey('ActivityTime.time_id'), nullable=False)
    timeslot_id_b = db.Column(db.Integer, db.ForeignKey('ActivityTimeslot.timeslot_id'), nullable=False)
    # Activity = db.relationship("Activity", back_populates="ActivityBooking")
    # ActivityTimeslot = db.relationship("ActivityTimeslot", back_populates="ActivityBooking")
    # ActivityTime = db.relationship("ActivityTime", back_populates="ActivityBooking")