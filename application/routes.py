from flask import Flask, render_template, request, url_for, redirect, flash, session

from application.forms import LoginForm, RegistrationForm, BookActivity, Password_Reset
from application import app, db, flask_change_password
from application.models import CustomerContact, CustomerLogin, Activity, ActivityBook



from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
# @app.route('/home')
def home():
    # if 'email' in session:
    #     email = session['email']
    #     user = CustomerContact.query.filter_by(first_name=email).first()
    #     return 'Logged in as ' + user + '<br>' + "<b><a href="url_for("login">Click here to log out</a></b>"
    #
    #
    #     return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"

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
    if request.method == "POST" and form.validate():
        email = request.form.get('email')
        password = request.form.get('password')


        user = CustomerLogin.query.filter_by(email_address=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details or sign-up for an account below.")

        else:
            return redirect(url_for('dashboard'))

    return render_template("login.html", title="login", form=form, error=flash)


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
    session.pop('email', None)
    return redirect(url_for('home'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_of_birth = form.date_of_birth.data
        phone_number = form.phone_number.data
        email_address = form.email_address.data
        address_line = form.address_line.data
        postcode = form.post_code.data
        city = form.city.data
        password = form.password.data
        details = CustomerContact(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, phone_number=phone_number, address_line=address_line, postcode=postcode, city=city,)
        login_d = CustomerLogin(email_address=email_address, password=generate_password_hash(password, method='sha256'))
        db.session.add(details)
        db.session.add(login_d)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', error=flash, form=form)


@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html', title='dashboard')


@app.route('/book', methods=['GET'])
def book():
    activities = db.session.query(Activity).all()
    return render_template('activities.html', title='Book', activities=activities)


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    form = BookActivity()

    if request.method == 'POST':
        booked = ActivityBook(email_address=form.email_address.data,
                              date=form.date.data,
                              activity_type=form.activity_type.data,
                              timeslot=form.timeslot.data)
        db.session.add(booked)
        db.session.commit()
        flash('Thanks for booking!')
        return redirect(url_for('my_bookings'))
    return render_template('booking.html', title='Booking', form=form)


@app.route('/my_bookings')
def my_bookings():
    return render_template('my_bookings.html', title='my_bookings')


@app.route('/policy')
def policy():
    return render_template('policy.html', title='policy')


@app.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    form = Password_Reset()
    if request.method == 'POST':
        try:
            email = form.email.data
            password = form.confirm_new_password.data
            user = CustomerLogin.query.filter_by(email_address=email).first()
            user.password = generate_password_hash(password, method='sha256')
            db.session.commit()
            flash('Your password has been updated!')
            return redirect(url_for('login'))
        except:
            flash('You do not have an account, please sign up below')

    return render_template('password_reset.html', form=form, title='password_reset')