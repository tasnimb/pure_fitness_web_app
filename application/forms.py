from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo


gender = ('Female', 'Male')


class RegistrationForm(FlaskForm):
    first_name = StringField('firstname',validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('lastname', validators=[DataRequired(), Length(min=2, max=20)])
    dob = DateField('dob', format='%y-%m-%d')
    email_address = StringField('Email',validators=[DataRequired(), Length(min=6, max=35)])
    contact_number = IntegerField('phone',validators=[DataRequired(), Length(min=4, max=25)]) # check out regex
    address = StringField('address',validators=[DataRequired(), Length(min=5, max=50)])
    post_code = StringField('postcode', validators=[DataRequired(), Length(min=8, max=10)])
    city = StringField('city', validators=[DataRequired(), Length(min=2, max=20)])
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
    booking_id = HiddenField()
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=35)])
    date = DateField('Class Date')
    activity = SelectField('Class', validators=[InputRequired()], choices=[('Strength', 'Strength'), ('Cardio', 'Cardio'),
                                        ('Mind and Body', 'Mind and Body'), ('Cycling', 'Cycling'), ('Swim', 'Swim')])
    activity_time = SelectField('Time of Day', validators=[InputRequired()], choices=[('1', 'Morning'),
                                                                    ('2', 'Afternoon'), ('3', 'Evening')])
    activity_timeslot = SelectField('Timeslot', validators=[InputRequired()], choices=[])
    Book = SubmitField('Book a Class')