#!/usr/bin/python3

""" Test .get() and .count() methods

"""

from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User


print("All objects: {}".format(storage.count()))
print("Place objects: {}".format(storage.count(Place)))
print("State objects: {}".format(storage.count(State)))



first_state_id = list(storage.all(State).values())[0].id

print("First state: {}".format(storage.get(State, first_state_id)))
print()
first_amen_id = list(storage.all(Place).values())[0].id
print("First place: {}".format(storage.get(Place, first_amen_id)))
print()
# fcd = list(storage.all(City).values())[0].state_id
# print("Associated state: {}".format(storage.get(City, fcd)))
