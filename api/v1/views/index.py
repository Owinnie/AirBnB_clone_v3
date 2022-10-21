#!/usr/bin/python3
"""Home page"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

# models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status: OK"""
    return jsonify({'status': 'OK'})


@app_views.route('/api/v1/stats', strict_slashes=False)
def stats():
    """Get no. of objs in storage using .count()"""
    classes = {"amenities": Amenity, "cities": City,
               "places": Place, "reviews": Review,
               "states": State, "users": User}
    json_dict = {}

    for name, cls in classes.items():
        json_dict.update({name: storage.count(cls)})

    return jsonify(json_dict)
