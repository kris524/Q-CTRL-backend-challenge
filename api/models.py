from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship, backref

# from main import db
from api import db

# Base = declarative_base()


class Person(db.Model):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    address = relationship("Address", back_populates="person", uselist=False)

    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "address": {
                "number": self.address.number,
                "street": self.address.street,
                "city": self.address.city,
                "state": self.address.state,
            },
        }

    # def insert_user(self,email, name, address):


class Address(db.Model):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))

    number = db.Column(db.Integer)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)

    person = relationship("Person", back_populates="address")

    def address_to_dict(self):
        return {
            "number": self.number,
            "street": self.street,
            "city": self.city,
            "state": self.state,
        }


# db.create_all()
# person1 = Person(email="adqqad@avc.gf", name="gogo")
# address1 = Address(number=1, street="lol", city="soz", state="rekt", person=person1)

# db.session.add(person1)
# db.session.commit()


# the_data = db.session.query(Person)

# for i in the_data:
#     print(i.email, i.name, i.address.street)
