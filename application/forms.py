from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


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
    account_number = IntegerField('accountnumber',validators=[DataRequired(), Length(min=8, max=8)])
    sort_code = IntegerField('sortcode',validators=[DataRequired(), Length(min=8, max=8)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    Login = SubmitField('Login')

