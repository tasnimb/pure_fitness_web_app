from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, SelectMultipleField, HiddenField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired


gender = ('Female', 'Male')


class RegistrationForm(FlaskForm):
    title = StringField('title',validators=[DataRequired(), Length(min=2, max=10)])
    first_name = StringField('firstname',validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('lastname', validators=[DataRequired(), Length(min=2, max=20)])
    dob = IntegerField('dob', validators=[DataRequired(), Length(min=8, max=10)])
    email = StringField('Email',validators=[DataRequired(), Length(min=6, max=35)])
    contact_number = IntegerField('phone',validators=[DataRequired(), Length(min=4, max=25)]) # check out regex
    Address = StringField('Address',validators=[DataRequired(), Length(min=5, max=50)])
    post_code = StringField('postcode', validators=[DataRequired(), Length(min=8, max=10)])
    city = StringField('city', validators=[DataRequired(), Length(min=2, max=20)])
    account_number = IntegerField('accountnumber', validators=[DataRequired(), Length(min=8, max=8)])
    sort_code = IntegerField('sortcode', validators=[DataRequired(), Length(min=8, max=8)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    Login = SubmitField('Login')


class BookActivity(FlaskForm):
    activity = [('1', 'Strength'), ('2', 'Cardio'), ('Mind and Body', 'Mind and Body'), ('Cycling', 'Cycling'), ('Swim', 'Swim')]
    time_day = [('1', 'Morning'), ('2', 'Afternoon'), ('3', 'Evening')]
    timeslot = [('z', "8am - 9am"), ('A', "9am - 10am"), ('B', "10am - 11am"), ('C', "11am - 12pm"),
                ('E', "12pm - 1pm"), ('F', "1pm - 2pm"), ('G', "2pm - 3pm"), ('H', "3pm - 4pm"), ('I', "4pm - 5pm"),
                ('J', "5pm - 6pm"), ('K', "6pm - 7pm"),
                ('L', "7pm - 8pm"), ('M', "8pm - 9pm"), ]

    booking_id = HiddenField()
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=35)])
    date = DateField('Date')
    activity_type = SelectField('Class', validators=[InputRequired()], choices=activity)
    time_day = SelectField('Time', validators=[InputRequired()], choices=time_day)
    activity_timeslot = SelectField('Timeslot', validators=[InputRequired()], choices=timeslot)
    book = SubmitField('Book a Class')

class BookType(FlaskForm):
    activity = [('1', 'Strength'), ('2', 'Cardio'), ('Mind and Body', 'Mind and Body'), ('Cycling', 'Cycling'), ('Swim', 'Swim')]


class BookTime(FlaskForm):
    time_day = [('1', 'Morning'), ('2', 'Afternoon'), ('3', 'Evening')]
    time_day = SelectField('Time', validators=[InputRequired()], choices=time_day)


class BookTimeslot(FlaskForm):
    timeslot = [('z', "8am - 9am"),('A', "9am - 10am"), ('B', "10am - 11am"), ('C', "11am - 12pm"), ('E', "12pm - 1pm"), ('F', "1pm - 2pm"),('G', "2pm - 3pm"), ('H', "3pm - 4pm"), ('I', "4pm - 5pm"), ('J', "5pm - 6pm"),('K',"6pm - 7pm"),
                                       ('L', "7pm - 8pm"),('M',"8pm - 9pm"),]

