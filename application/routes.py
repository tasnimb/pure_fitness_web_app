from flask import Flask, render_template, request, url_for, redirect
from application.forms import *
from application import app, db, models
from application.models import *
from datetime import date
from sqlalchemy.orm import load_only
import pprint
pp = pprint.PrettyPrinter(indent=4)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


def openLogin():
    return redirect(url_for('login'))


@app.route('/book', methods=['GET'])
def book():
    activities = db.session.query(Activity).all()
    return render_template('activities.html', title='Book', activities=activities)

#
# @app.route('/book', methods=['GET'])
# def book():
#     activities = db.session.query(Activity).all()
#     # activities = Activity.query.all()
#     app.logger.info(str(activities))
#     app.logger.info("LOGGING")
#     return render_template('activities.html', title='Book', activities=activities)


@app.route('/booking.html', methods=['GET', 'POST'])
def booking():

    # app.logger.info("LOG")
    # app.logger.info(str(form.__dict__))
    # if not current_user.is_authenticated:
    #     flash('Please Log in as admin to add team')
    #     return redirect(url_for('login'))
    # if current_user.is_authenticated:
    #     return redirect(url_for('/booking.html'))

    form=BookActivity()
    if request.method == "POST":
        if form.validate_on_submit():
            booking = BookActivity(email_address=form.email_address.data,
                        date=form.date.data,
                        activity_type_id_b=form.activity_type_id_b.data,
                        time_day_b=form.time_day_b.data,
                        atimeslot_id_b=form.timeslot_id_b.data)
            # message = f"Thank you, for booking {activity}."
            db.session.add(booking)
            db.session.commit()
            return redirect(url_for('my_bookings'))

    return render_template('booking.html', title='Booking', form=form)


# #activity_timeslot.query.filter_by(id=form.timelost.data).first())
# @app.route('/timeslot/<day_time_id>')
# def timeslot(day_time_id):
#     timeslot = ActivityTimeslot.query.filter_by(day_time_id=day_time_id).all()
#
#     timeslot_list = []
#
#     for timeslot in ActivityTimeslot:
#         timeslot_obj = {}
#         timeslot_obj['id'] = ActivityTimeslot.timeslot_id
#         timeslot_obj['name'] = ActivityTimeslot.timeslot
#         timeslot_list.append(timeslot_obj)
#
#     return jasonify({'timeslot' : timeslot_list)



# @app.route('/my_bookings', methods=['GET', 'POST', 'UPDATE/MODIFY', 'DELETE'])
# def my_bookings(search):
#     bookings = []
#     search_string = search.data['search']
#
# To search for all the bookings for email_address
# session.query(BookActivity).filter(BookActivity.email_address=='<input>')
#
# # to delete a booking_id (but they have to know the booking id ???
# activity_to_delete = session.query(BookActivity).filter(BookActivity.booking_id==<id>).first()
# session.delete(activity_to_delete)
# session.commit()
#     if not current_user.is_authenticated:
#         flash('Please Log in as admin to add team')
#         return redirect(url_for('login'))
#     if search.data['search'] == '':
#         qry = db.session.query(Activity)
#         bookings = qry.all()
#
    #
    # bookings = ActivityBooking.query.filter_by(date=date).all()
    # meetings = Meeting.query.filter_by(teamId=team.id).all()
    # hasFutureBooking = False
    # for booking in bookings:
    #     if meeting.date >= datetime.now(): \
    # my_data = db.session.query(query).filter(
    #     func.date(BookActivity.date) >= date.today()
    # ).all()


@app.route('/my_bookings')
def my_bookings():
    # activities = db.session.query(BookActivity).all()

    my_query = db.session.query(BookActivity, Activity, ActivityTime, ActivityTimeslot).join(Activity).join(
        ActivityTime).join(ActivityTimeslot)
    fields = ['email_address', 'date', 'activity_type', 'activity_timeslot']
    selected = db.session.query(my_query).options(load_only(*fields)).all()

    if not my_query:
        flash('No bookings found! Please visit our booking page to book.')
        return redirect(url_for('/booking'))

    return render_template('my_bookings.html', title='MyBookings', selected=selected)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/policy')
def policy():
    return render_template('policy.html', title='policy')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == "POST" and form.validate():
        email = form.email.data
        password = form.password.data

        if len(email) == 0 or len(password) == 0:
            error = "Please enter your email address and password"
        else:
            return "You are now logged in "
    return render_template("login.html", title="login", form=form, message=error)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm(request.form)
#     if request.method == 'POST' and form.validate():
#         user = User(form.username.data, form.email.data,
#                     form.password.data)
#         db_session.add(CustomerLogin)
#         flash('Thanks for registering')
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)

# how to tell if a user is logged in
# https://stackoverflow.com/questions/35636678/displaying-jinja2-form-fields-based-on-attribute-value


