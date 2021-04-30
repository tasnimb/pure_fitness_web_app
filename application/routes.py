from flask import Flask,g, render_template, request, url_for, redirect, flash, session
from datetime import timedelta
from application.forms import LoginForm, RegistrationForm, BookedActivity, Password_Reset, Qns
from application import app, db
from application.models import CustomerContact, CustomerLogin, Activity, ActivityBooked, Faq
from werkzeug.security import generate_password_hash, check_password_hash


app.permanent_session_lifetime=timedelta(minutes=1)


# @app.before_request
# def before_request():
#     if '' in session:
#         CustomerLogin.query.filter_by(email_address=email).first()


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == "POST" and form.validate():
        email = request.form.get('email')
        password = request.form.get('password')
        session.permanent = True

        user = CustomerLogin.query.filter_by(email_address=email).first()
        user2 = email
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details or sign-up for an account below.")

        else:

            session["user2"] = user2
            if "user2" in session:
                return redirect(url_for('dashboard'))

    return render_template("login.html", title="login", form=form, error=flash)


@app.route('/dashboard')
def dashboard():
    if "user2" in session:
        user2 = session["user2"]
        return render_template('dashboard.html',user=user2)
    else:
        return redirect(url_for('login'))
    # return render_template('dashboard.html', title='Members Area')


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
    session.pop('user2', None)
    return redirect(url_for('login'))


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


@app.route('/profile')
def profile():

    return render_template('profile.html', title='profile')


@app.route('/book', methods=['GET'])
def book():
    activities = db.session.query(Activity).all()
    return render_template('activities.html', title='Book', activities=activities)


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    form = BookedActivity()

    if request.method == 'POST':
        email_address = request.form.get('email_address')
        booked = ActivityBooked(email_address=form.email_address.data,
                                date=form.date.data,
                                activity_type=form.activity_type.data,
                                timeslot=form.timeslot.data)
        db.session.add(booked)
        db.session.commit()
        flash('Thanks for booking!')
        return redirect(url_for('my_bookings'))
    return render_template('booking.html', title='Book Class', form=form)


@app.route('/my_bookings')
def my_bookings():
    # # email_address = request.form.get('email_address')
    # booking_class = BookedActivity.query.filter(BookedActivity.email_address == email_address).all()
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Qns()
    if request.method == 'POST':
        email_address = request.form.get('email_address')
        question = Faq(name=form.name.data,
                       email_address=form.email_address.data,
                       subject=form.subject.data,
                       question=form.question.data)
        db.session.add(question)
        db.session.commit()
        flash('The form has been submitted.')
        return redirect(url_for("contact_feedback", email_address=email_address))
    return render_template('contact.html', title='Contact', form=form)


@app.route('/contact_feedback/<email_address>')
def contact_feedback(email_address):
    comment = Faq.query.filter(Faq.email_address == email_address).all()
    return render_template('contact_feedback.html', comment=comment, title='My Contact')