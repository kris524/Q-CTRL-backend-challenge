from .models import Person


def resolve_persons(obj, info):
    try:
        persons = [person.to_dict() for person in Person.query.all()]
        payload = {"persons": persons}
    except Exception as error:
        print("222")
        payload = {"errors": [str(error)]}
    return payload
