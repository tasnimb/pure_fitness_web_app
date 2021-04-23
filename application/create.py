from application import db
from models import CustomerName, CustomerContact, City, Postcode

db.drop_all()
db.create_all()


personcity= City(city='London')
personpostcode = Postcode(postcode='w5 orw')
testPerson1=CustomerName(first_name='Tasnim',last_name='Begum')
testPerson2=CustomerContact(customer_name_id=1,phone_number='07497500204', email_address='tasnim.b98@gmail.com',
                            address_line='28 london street', postcode_id=1, city_id=1)





db.session.add(testPerson1)
db.session.add(testPerson2)
db.session.add(personcity)
db.session.add(personpostcode)

db.session.commit()