from .models import Person


def resolve_persons(obj, info):

    persons = [person.to_dict() for person in Person.query.all()]
    payload = {
        "email": persons[0]["email"],
        "name": persons[0]["name"],
        "address": [persons[0]["address"]],
    }

    return payload
