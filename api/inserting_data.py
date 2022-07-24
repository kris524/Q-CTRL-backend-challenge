from main import db
from api.models import Person, Address



db.create_all()
person1 = Person(email="adqqad@avc.gf", name="gogo")
address1 = Address(number=1, street="lol", city="soz", state="rekt", person=person1)

db.session.add(person1)
db.session.commit()


the_data = db.session.query(Person)

for i in the_data:
    print(i.to_dict())
