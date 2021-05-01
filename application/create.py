from application import app, db
from models import *

db.reflect()
db.drop_all()
db.create_all()


testPerson1a = User(first_name='Tasnim', last_name='Begum',email='tasnim.b98@gmail.com',date_of_birth='1998-09-08', phone_number='07497500204', address='28 London Street', postcode="KT5 8AT",  city="Nottingham",password="forgot!")
testPerson2a = User(first_name='Dwayne', last_name='Johnson', email='dwayne@fastcars.com',phone_number='07946183457',date_of_birth='1972-05-01', address='1 The Green', postcode="SE11 5SS",  city="Reading",password="ringonit")
testPerson3a = User(first_name='Beyonce', last_name='Knowles-Carter',email='beyonce@halo.com',  date_of_birth='1981-09-04', phone_number='07946512396', address='21 Jump Street', postcode="B2P AJ9",  city="Birmingham",password="yourewelcome")

db.session.add(testPerson1a)
db.session.add(testPerson2a)
db.session.add(testPerson3a)


# activity_time_a = ActivityTime(activity_time="Morning")
# activity_time_b = ActivityTime(activity_time="Afternoon")
# activity_time_c = ActivityTime(activity_time="Evening")
#
# db.session.add(activity_time_a)
# db.session.add(activity_time_b)
# db.session.add(activity_time_c)
#
# activity_timeslot_a = ActivityTimeslot(activity_timeslot="8am - 9am", day_time_id=1)
# activity_timeslot_b = ActivityTimeslot(activity_timeslot="9am - 10am", day_time_id=1)
# activity_timeslot_c = ActivityTimeslot(activity_timeslot="10am - 11am", day_time_id=1)
# activity_timeslot_d = ActivityTimeslot(activity_timeslot="11am - 12pm", day_time_id=1)
# activity_timeslot_e = ActivityTimeslot(activity_timeslot="12pm - 1pm", day_time_id=2)
# activity_timeslot_f = ActivityTimeslot(activity_timeslot="1pm - 2pm", day_time_id=2)
# activity_timeslot_g = ActivityTimeslot(activity_timeslot="2pm - 3pm", day_time_id=2)
# activity_timeslot_h = ActivityTimeslot(activity_timeslot="3pm - 4pm", day_time_id=2)
# activity_timeslot_i = ActivityTimeslot(activity_timeslot="4pm - 5pm", day_time_id=2)
# activity_timeslot_j = ActivityTimeslot(activity_timeslot="5pm - 6pm", day_time_id=2)
# activity_timeslot_k = ActivityTimeslot(activity_timeslot="6pm - 7pm", day_time_id=3)
# activity_timeslot_l = ActivityTimeslot(activity_timeslot="7pm - 8pm", day_time_id=3)
# activity_timeslot_m = ActivityTimeslot(activity_timeslot="8pm - 9pm", day_time_id=3)
#
# db.session.add(activity_timeslot_a)
# db.session.add(activity_timeslot_b)
# db.session.add(activity_timeslot_c)
# db.session.add(activity_timeslot_d)
# db.session.add(activity_timeslot_e)
# db.session.add(activity_timeslot_f)
# db.session.add(activity_timeslot_g)
# db.session.add(activity_timeslot_h)
# db.session.add(activity_timeslot_i)
# db.session.add(activity_timeslot_j)
# db.session.add(activity_timeslot_k)
# db.session.add(activity_timeslot_l)
# db.session.add(activity_timeslot_m)

activity_strength = Activity(activity_type="Strength",
                             activity_description="This all-time classic class uses high intensity "
                                "strength exercises to sculpt and tone your body whilst building endurance.",
                             duration="60 minutes",
                             instructor_name="Sujani Ajit")

activity_cardio = Activity(activity_type="Cardio",
                           activity_description="This sure-fire way to improve your cardio efficiency, increase strength"
                            " and burn calories uses equipment such as medicine balls, kettlebells and an assault bike.",
                           duration="45 minutes",
                           instructor_name="Te-Yu Hung")

activity_mnb = Activity(activity_type="Mind and Body",
                        activity_description="Experience a total body stretch to leave you feeling refreshed and restored."
                        " This full body stretching class is designed to tone the body while burning fat and defining "
                        "muscles.",
                        duration="60 minutes",
                        instructor_name="Ilka Breytenbach")

activity_cycling = Activity(activity_type="Cycling",
                            activity_description="Get ready to work up a sweat and burn a serious number"
                            " of calories. This class focuses on endurance, strength, intervals, high intensity and "
                            "recovery Using indoor stationary bikes.",
                            duration="45 minutes",
                            instructor_name="Muhammad Begum")

activity_swim = Activity(activity_type="Swim",
                         activity_description="Water aerobics will help to build cardiovascular strength and "
                            "tone your muscles with a low impact routine.",
                         duration="30 minutes",
                         instructor_name="Jenna Stephens")

db.session.add(activity_strength)
db.session.add(activity_cardio)
db.session.add(activity_mnb)
db.session.add(activity_cycling)
db.session.add(activity_swim)

db.session.commit()
