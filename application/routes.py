from flask import Flask, g, render_template, request, url_for, redirect, flash, session
from datetime import timedelta, date
from application.forms import LoginForm, RegistrationForm, BookedActivity, PasswordReset, Qns, DeleteBooking, DeleteAccount
from application import app, db,login_manager
from application.models import User, Activity, ActivityBooked, Faq
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc, func, delete
from flask_login import login_user,logout_user,current_user,login_required

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
    if request.method == "POST" and form.validate():

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details or sign-up for an account below.")

        else:
            login_user(user)
            flash(f'Login successful{user.first_name}',category='success')


            return redirect(url_for('dashboard'))

    return render_template("login.html", title="login", form=form, error=flash)


@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(id=current_user.id).first()

    return render_template('dashboard.html',user=user.first_name)


@app.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('login'))




@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if request.method == 'POST':
        first_name = form.first_name.data,
        last_name = form.last_name.data,
        date_of_birth = form.date_of_birth.data,
        phone_number = form.phone_number.data,
        email = form.email.data,
        address_line = form.address.data,
        postcode = form.postcode.data,
        city = form.city.data,
        password = form.password.data


        details=User(first_name=first_name,last_name=last_name,email=email,date_of_birth=date_of_birth,
                     phone_number=phone_number,address=address_line,
                     postcode=postcode,city=city,password=generate_password_hash(password, method='sha256'))

        db.session.add(details)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', error=flash, form=form)


@app.route('/profile')
@login_required
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
            user = User.query.filter_by(email_address=email).first()
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


@app.route('/delete_account', methods=['GET', 'POST'])
def delete_account():
    form = DeleteAccount()
    if request.method == "POST":
        try:
            email = request.form.get('email')
            user = User.query.filter_by(email_address=email).first()
            db.session.delete(user)
            db.session.commit()
            flash('Your account has been deleted.')
            return redirect(url_for('login'))
        except:
            flash("This account has already been deleted or it does not exist")
    return render_template('delete_account.html', form=form, title='Delete Account')

