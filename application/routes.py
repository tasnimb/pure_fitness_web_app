import datetime
from flask import Flask, g, render_template, request, url_for, redirect, flash
from datetime import timedelta, date
from application.forms import LoginForm, RegistrationForm, BookedActivity, PasswordReset, Qns, DeleteBooking, DeleteAccount
from application import app, db, login_manager
from application.models import User, Activity, ActivityBooked, Faq
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc, func, delete
from flask_login import login_user, logout_user, current_user, login_required

app.permanent_session_lifetime = timedelta(minutes=60)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@app.route('/')
# @app.route('/home')
def home():

    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    error = ""
    form = LoginForm()
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details or sign-up for an account below.")

        else:
            login_user(user)

            return redirect(url_for('dashboard'))

    return render_template("login.html", title="login", form=form, error=flash)


@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(id=current_user.id).first()

    return render_template('dashboard.html', user=user.first_name)


@app.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    try:
        if request.method == 'POST':
            membership = form.select_membership.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            date_of_birth = form.date_of_birth.data,
            phone_number = form.phone_number.data,
            email = form.email.data,
            address_line = form.address.data,
            postcode = form.postcode.data,
            city = form.city.data,
            password = form.password.data

            details = User(select_membership=membership,first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth,
                     phone_number=phone_number, address=address_line,
                     postcode=postcode, city=city, password=generate_password_hash(password, method='sha256'))

            db.session.add(details)
            db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for('login'))
    except:
        flash('An account associated to this email address already exists. Please login or reset your password')
    return render_template('register.html', error=flash, form=form)


@app.route('/profile')
@login_required
def profile():
    if current_user.is_authenticated:
        info = db.session.query(User).filter(User.id == current_user.get_id()).first()
        return render_template('profile.html', info=info, title='Profile')


@app.route('/book')
def book():
    activities = db.session.query(Activity).all()
    return render_template('activities.html', title='Book a class', activities=activities)


# @app.route('/booking', methods=['GET', 'POST'])
# def booking():
#     form = BookedActivity()
#     if current_user.is_authenticated:
#         if request.method == 'POST':
#             if form.date.data > date.today():
#                 result = db.session.query(User, ActivityBooked).filter(User.email==ActivityBooked.email_address,
#                                                             User.id==current_user.get_id()).first()
#                 booked = ActivityBooked(email_address=result.ActivityBooked.email_address,
#                                          date=form.date.data,
#                                          activity_type=form.activity_type.data,
#                                          timeslot=form.timeslot.data)
#                 db.session.add(booked)
#                 db.session.commit()
#                 flash('Thanks for booking!')
#                 return redirect(url_for('my_bookings'))
#         else:
#             flash("Please make your selection.")
#     return render_template('booking.html', title='Book Class', form=form)

@app.route('/booking', methods=['GET', 'POST'])
@login_required
def booking():
    form = BookedActivity()
    if current_user.is_authenticated:
        if request.method == 'POST':
            date_limit = date.today() + datetime.timedelta(days=14)
            if (form.date.data > date.today()) and (form.date.data <= date_limit):
                result = db.session.query(User).filter(User.id == current_user.get_id()).first()
                booked = ActivityBooked(email_address=result.email,
                                        date=form.date.data,
                                        activity_type=form.activity_type.data,
                                        timeslot=form.timeslot.data)
                db.session.add(booked)
                db.session.commit()
                flash('Thanks for booking!')
                return redirect(url_for('my_bookings'))
            else:
                flash("Please check your dates.")
                return redirect(url_for('booking'))
        else:
            flash("Please make your selection.")
    return render_template('booking.html', title='Book Class', form=form)


@app.route('/my_bookings', methods=['GET', 'POST', 'DELETE'])
@login_required
def my_bookings():
    result = db.session.query(User).filter(User.id == current_user.get_id()).first()
    email_address = result.email
    if current_user.is_authenticated:
        current = db.session.query(ActivityBooked).filter(ActivityBooked.email_address == email_address, ActivityBooked.date
                                                          >= func.current_date()).order_by(ActivityBooked.date).all()
        past = db.session.query(ActivityBooked).filter(ActivityBooked.email_address == email_address, ActivityBooked.date <
                                                       func.current_date()).order_by(ActivityBooked.date).all()

    form = DeleteBooking()
    if request.method == "POST":
        if (form.booking_id.data != form.confirm_id.data):
            flash("The Confirm Booking ID is different. Please ensure Booking ID numbers are the same.")
        else:
            try:
                booked = request.form.get('booking_id')
                activity = db.session.query(User, ActivityBooked).filter(User.email == ActivityBooked.email_address,
                                                                        User.id == current_user.get_id(),
                                                                        ActivityBooked.booking_id==booked,
                                                                        ActivityBooked.date >= func.current_date()).first()
                activity_to_delete = ActivityBooked.query.filter_by(booking_id=activity.ActivityBooked.booking_id).first()
                db.session.delete(activity_to_delete)
                db.session.commit()
                flash('Result! Your booking has been cancelled.')
                return redirect(url_for('my_bookings'))
            except Exception as error:
                flash("Booking ID error. Please check the ID or contact our centre for support")

    return render_template('my_bookings.html', current=current, past=past, form=form, title='My Bookings')


@app.route('/policy')
def policy():
    return render_template('policy.html', title='policy')


@app.route('/password_reset', methods=['GET', 'POST'])
@login_required
def password_reset():
    form = PasswordReset()
    if request.method == 'POST':
        try:
            email = form.email.data
            password = form.confirm_new_password.data
            user = User.query.filter_by(email=email).first()
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
    comment = Faq.query.filter(Faq.email_address == email_address).order_by(Faq.faq_id.desc()).first()
    return render_template('contact_feedback.html', comment=comment, title='My Contact')


@app.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    if current_user.is_authenticated:
        account = db.session.query(User).filter(User.id == current_user.get_id()).first()
    form = DeleteAccount()
    if request.method == "POST":
        try:
            # password = request.form.get('password')
            db.session.delete(account)
            db.session.commit()
            flash('Your account has been deleted.')
            return redirect(url_for('login'))
        except:
            flash("This account has already been deleted or it does not exist")
    return render_template('delete_account.html', form=form, title='Delete Account')
