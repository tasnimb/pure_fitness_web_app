from flask import Flask
from application import app, db


class CustomerContact(db.Model):
    __tablename__ = 'Customer Contact'
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(15))
    address_line = db.Column(db.String(70))
    postcode = db.Column(db.String(8))
    city = db.Column(db.String(20))


class CustomerLogin(db.Model):
    __tablename__ = 'Customer Login'
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