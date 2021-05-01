from application import app, db
from models import *

db.reflect()
db.drop_all()
db.create_all()


testPerson1a = User(first_name='Tasnim', last_name='Begum',email='tasnim.b98@gmail.com',date_of_birth='1998-09-08', phone_number='07497500204', address='28 London Street', postcode="KT5 8AT",  city="Nottingham",password="sha256$n2JF3o03$9f93108a285f8dc675c9371c14f69dd16758ed5278ae0ca7728c7c1242c6cf88")
testPerson2a = User(first_name='Dwayne', last_name='Johnson', email='dwayne@fastcars.com',phone_number='07946183457',date_of_birth='1972-05-01', address='1 The Green', postcode="SE11 5SS",  city="Reading",password="sha256$n2JF3o03$9f93108a285f8dc675c9371c14f69dd16758ed5278ae0ca7728c7c1242c6cf88")
testPerson3a = User(first_name='Beyonce', last_name='Knowles-Carter',email='beyonce@halo.com',  date_of_birth='1981-09-04', phone_number='07946512396', address='21 Jump Street', postcode="B2P AJ9",  city="Birmingham",password="sha256$n2JF3o03$9f93108a285f8dc675c9371c14f69dd16758ed5278ae0ca7728c7c1242c6cf88")

db.session.add(testPerson1a)
db.session.add(testPerson2a)
db.session.add(testPerson3a)
booking_b = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-02', activity_type="Swim", timeslot="9am - 10am")
booking_a = ActivityBooked(email_address="dwayne@fastcars.com",  date='2021-03-12', activity_type="Cardio", timeslot="9am - 10am")
booking_c = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-02-09', activity_type="Cycling", timeslot="9am - 10am")
booking_d = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-02', activity_type="Swim", timeslot="9am - 10am")
booking_e = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-03-18', activity_type="Strength", timeslot="9am - 10am")
booking_f = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-24', activity_type="Strength", timeslot="9am - 10am")
booking_g = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-12', activity_type="Cardio", timeslot="9am - 10am")
booking_h = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-09', activity_type="Swim", timeslot="9am - 10am")
booking_i = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-04-12', activity_type="Cardio", timeslot="9am - 10am")


booking_b = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-02', activity_type="Swim", timeslot="9am - 10am")
booking_a = ActivityBooked(email_address="dwayne@fastcars.com",  date='2021-03-12', activity_type="Cardio", timeslot="9am - 10am")
booking_c = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-02-09', activity_type="Cycling", timeslot="9am - 10am")
booking_d = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-02', activity_type="Swim", timeslot="9am - 10am")
booking_e = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-03-18', activity_type="Strength", timeslot="9am - 10am")
booking_f = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-24', activity_type="Strength", timeslot="9am - 10am")
booking_g = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-12', activity_type="Cardio", timeslot="9am - 10am")
booking_h = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-05-09', activity_type="Swim", timeslot="9am - 10am")
booking_i = ActivityBooked(email_address="dwayne@fastcars.com", date='2021-04-12', activity_type="Cardio", timeslot="9am - 10am")
#
db.session.add(booking_a)
db.session.add(booking_b)
db.session.add(booking_c)
db.session.add(booking_d)
db.session.add(booking_e)
db.session.add(booking_f)
db.session.add(booking_g)
db.session.add(booking_h)
db.session.add(booking_i)


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
