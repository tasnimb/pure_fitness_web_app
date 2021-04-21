from flask import Flask
from application import app,db
from sqlalchemy.orm import relationship

class CustomerName(db.Model):
    __tablename__='CustomerName'
    customer_name_id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30),nullable=False)
    last_name=db.Column(db.String(30),nullable=False)
    # contact=relationship('CustomerContact')

# class CustomerContact(db.Model):
#     __tablename__ = 'CustomerContact'
#     customer_id= db.Column(db.Integer,primary_key=True)
#     customer_name_id=db.Column(db.Integer,db.ForeignKey('CustomerName.customer_name_id'))
#     phone_number=db.Column(db.String(15))
#     email_address=db.Column(db.String(50),unique=True)
#     address_line=db.Column(db.String(70))
#     postcode=db.Column(db.String(10))
#     city_id=db.Column(db.Integer,db.ForeignKey('City.city_id'))

# class PostCode(db.Model):
#     __tablename__='PostCode'
#     postcode_id=db.Column(db.Integer,primary_key=True)
#     postcode=db.Column(db.String(8))
#     city_id=db.Column(db.String(20),db.ForeignKey(''))
