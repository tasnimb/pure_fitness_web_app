from application import db
from models import CustomerName

db.drop_all()
db.create_all()

testPerson1=CustomerName(first_name='Tasnim',last_name='Begum')

db.session.add(testPerson1)
db.session.commit()