from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from main import db

# Base = declarative_base()


class Person(db.Model):
    email = db.Column(db.String)
    name = db.Column(db.String)
    address = relationship("Address", uselist=False)
    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "description": self.address,
        }


class Address(db.Model):
    number = db.Column(db.Integer)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)

    person = relationship("Person")
