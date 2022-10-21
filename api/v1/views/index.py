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
    ls_of_cls = {"amenities": Amenity,
                 "cities": City,
                 "places": Place,
                 "reviews": Review,
                 "states": State,
                 "users": User}
    cnt_dict = {k: storage.count(v) for k, v in ls_of_cls.items()}
    return jsonify(cnt_dict)
