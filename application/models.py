from flask import Flask
from application import app,db
from sqlalchemy.orm import relationship


class CustomerName(db.Model):
    __tablename__ = 'Customer Name'
    customer_name_id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30),nullable=False)
    last_name=db.Column(db.String(30),nullable=False)
    # contact=db.relationship('CustomerContact')


class CustomerContact(db.Model):
    __tablename__ = 'Customer Contact'
    customer_id= db.Column(db.Integer,primary_key=True)
    customer_name_id=db.Column(db.Integer,db.ForeignKey('Customer Name.customer_name_id'))
    phone_number=db.Column(db.String(15))
    email_address=db.Column(db.String(50),unique=True)
    address_line=db.Column(db.String(70))
    postcode_id=db.Column(db.Integer, db.ForeignKey('Postcode.postcode_id'))
    city_id=db.Column(db.Integer,db.ForeignKey('City.city_id'))
    # customername = db.relationship("CustomerName", back_populates="customer contact")


class City(db.Model):
    __tablename__ = 'City'
    city_id=db.Column(db.Integer,primary_key=True)
    city = db.Column(db.String(20))


class Postcode(db.Model):
    __tablename__ = 'Postcode'
    postcode_id=db.Column(db.Integer,primary_key=True)
    postcode=db.Column(db.String(8))

class CustomerLogin(db.Model):
    __tablename__ = 'Customer Login'
    customerlogin_id = db.Column(db.Integer,primary_key=True)
    email_address = db.Column(db.String(50), db.ForeignKey('CustomerContact.email_address.id'))
    password = db.Column(db.String(8))


#
# class SessionTimetable(db.Model):
#     __tablename__ = 'Session Time Table'
#     session_time_id = db.Column(db.Integer, primary_key=True)
#     session_time = db.Column(db.String(30), nullable=False)
#     session_day = db.Column(db.String(15), nullable=False, unique=True)
#     # instructor_id = db.Column(db.Integer, db.Foreign_key('Instructor.instructor_id'))
#     session_type_id = db.Column(db.Integer, db.ForeignKey('Session.session_type_id'))
#
# # class Instructor(db.Model):
# #     __tablename__ = 'Instructor'
# #     instructor_id = db.Column(db.Integer, primary_key=True)
# #     full_name = db.Column(db.String(30), nullable=False)
#
# class Session(db.Model):
#     __tablename__ = 'Session'
#     session_type_id = db.Column(db.Integer, primary_key=True)
#     session_type = db.Column(db.String(30), nullable=False, unique=True)
#
# class SessionBooking(db.Model):
#     __tablename__ = 'Session Booking'
#     booking_id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('CustomerContacts.customer_id'))
#     session_time_id = db.Column(db.Integer, db.ForeignKey('SessionTimetable.session_time_id'))
