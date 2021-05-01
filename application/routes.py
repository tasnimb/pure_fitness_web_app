from flask import Flask, g, render_template, request, url_for, redirect, flash, session
from datetime import timedelta, date
from application.forms import LoginForm, RegistrationForm, BookedActivity, PasswordReset, Qns, DeleteBooking
from application import app, db
from application.models import CustomerContact, CustomerLogin, Activity, ActivityBooked, Faq
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc, func, delete

app.permanent_session_lifetime = timedelta(minutes=60)


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
        username = email
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details or sign-up for an account below.")

        else:

            session["username"] = username
            if "username" in session:
                return redirect(url_for('dashboard', username=username))

    return render_template("login.html", title="login", form=form, error=flash)


@app.route('/dashboard/')
def dashboard():
    if "username" in session:
        username = session["username"]
        #email_address = request.form.get('email')
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))
    #return render_template('dashboard.html', title='Members Area')


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


@app.route('/book')
def book():
    activities = db.session.query(Activity).all()
    return render_template('activities.html', title='Book a class', activities=activities)


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    form = BookedActivity()
    if "username" in session:
        username = session["username"]

        if request.method == 'POST':
            if "username" in session:
                username = session["username"]
                if form.date.data > date.today():
                    booked = ActivityBooked(email_address=username,
                                            date=form.date.data,
                                            activity_type=form.activity_type.data,
                                            timeslot=form.timeslot.data)
                    db.session.add(booked)
                    db.session.commit()
                    flash('Thanks for booking!')
                    return redirect(url_for('my_bookings', username=username))
                else:
                    flash("Cannot book dates in the past.")
    return render_template('booking.html', title='Book Class', form=form)


@app.route('/my_bookings', methods=['GET', 'POST', 'DELETE'])
def my_bookings():
    if "username" in session:
        username = session["username"]
        current = db.session.query(ActivityBooked).filter(ActivityBooked.email_address == username, ActivityBooked.date
                                                          >= func.current_date()).order_by(ActivityBooked.date).all()
        past = db.session.query(ActivityBooked).filter(ActivityBooked.email_address == username, ActivityBooked.date <
                                                       func.current_date()).order_by(ActivityBooked.date).all()
    form = DeleteBooking()
    if request.method == "POST":
        try:
            booked = request.form.get('booking_id')
            activity = ActivityBooked.query.filter_by(booking_id=booked).first()
            db.session.delete(activity)
            db.session.commit()
            flash('Your booking has been cancelled.')
            return redirect(url_for('my_bookings', username=username))
        except ValueError:
            flash("The booking cannot be deleted. Please contact our centre for support")
        except:
            flash("The booking cannot be deleted. Please contact our centre for support")

    return render_template('my_bookings.html', username=username, current=current, past=past, form=form, title='My Bookings')


@app.route('/policy')
def policy():
    return render_template('policy.html', title='policy')


@app.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    form = PasswordReset()
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

    return render_template('password_reset.html', form=form, title='Password Reset')


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
    comment = Faq.query.filter(Faq.email_address == email_address).first()
    return render_template('contact_feedback.html', comment=comment, title='My Contact')
