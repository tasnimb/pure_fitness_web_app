from flask import Flask, render_template, request, url_for, redirect, flash
from application.forms import LoginForm, RegistrationForm
from application import app, db
from application.models import CustomerContact, CustomerName, Postcode, City, CustomerLogin, Activity


@app.route('/')
# @app.route('/home')
def home():
    return render_template('home.html', title='Home')


def openLogin():
    return redirect(url_for('login'))


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    # if form.validate_on_submit()
    # user = CustomerLogin.query.get(form.email_address.data)
    #     if user:
    #         if password(user.password, form.password.data):

    if request.method == "POST" and form.validate():
        email = form.email.data
        password = form.password.data

        if len(email) == 0 or len(password) == 0:
            error = "Please enter your email address and password"
        else:
            return redirect(url_for('dashboard'))
    return render_template("login.html", title="login", form=form, message=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        first_name=form.first_name.data
        last_name=form.last_name.data
        phone_number=form.phone_number.data
        email_address=form.email_address.data
        address_line=form.address_line.data
        postcode=form.post_code.data
        city=form.city.data
        password=form.password.data
        name = CustomerName(first_name=first_name,last_name=last_name)
        details = CustomerContact(phone_number=phone_number,address_line=address_line)
        postcode = Postcode(postcode=postcode)
        city = City(city=city)
        login_d = CustomerLogin(email_address=email_address,password=password)
        db.session.add(name)
        db.session.add(details)
        db.session.add(postcode)
        db.session.add(city)
        db.session.add(login_d)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='dashboard')


@app.route('/book', methods=['GET'])
def book():
    activities = db.session.query(Activity).all()
    return render_template('activities.html', title='Book', activities=activities)


@app.route('/booking')
def booking():
    return render_template('booking.html', title='booking')


@app.route('/my_bookings')
def my_bookings():
    return render_template('my_bookings.html', title='my_bookings')


@app.route('/policy')
def policy():
    return render_template('policy.html', title='policy')
