from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField


gender = ('Female', 'Male')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    date_of_birth = DateField('Date-of-birth', format='%Y-%m-%d')
    email_address = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
    phone_number = IntegerField('Phone', validators=[DataRequired(), Length(min=4, max=25)]) # check out regex
    address_line = StringField('Address', validators=[DataRequired(), Length(min=5, max=50)])
    post_code = StringField('Postcode', validators=[DataRequired(), Length(min=8, max=10)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    Login = SubmitField('Login')


class Password_Reset(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Update Password')


class Qns(FlaskForm):
    subjects = [('Registration Support', 'Registration Support'), ('Booking Support', 'Booking Support'),
                ('Complaint or Grievance', 'Complaint or Grievance'), ('Feedback', 'Feedback'), ('Other', 'Other')]
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=100)])
    email_address = StringField('Email', validators=[DataRequired(), Email()])
    subject = SelectField('Subject', validators=[DataRequired()], choices=subjects)
    question = StringField('Question/Comment', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit')


class BookedActivity(FlaskForm):
    activity = [('Strength', 'Strength'), ('Cardio', 'Cardio'), ('Mind and Body', 'Mind and Body'), ('Cycling', 'Cycling'),
                ('Swim', 'Swim')]
    timeslot = [("9am - 10am", "9am - 10am"), ("11am - 12pm", "11am - 12pm"), ("1pm - 2pm", "1pm - 2pm"), ("3pm - 4pm", "3pm - 4pm"),
                ("5pm - 6pm", "5pm - 6pm"), ("7pm - 8pm", "7pm - 8pm"), ]
    email_address = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
    date = DateField('Date', format='%Y-%m-%d')
    activity_type = SelectField('Class', validators=[DataRequired()], choices=activity)
    timeslot = SelectField('Timeslot', validators=[DataRequired()], choices=timeslot)
    submit = SubmitField('Book')
