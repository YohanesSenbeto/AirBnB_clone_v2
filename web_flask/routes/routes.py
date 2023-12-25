#!/usr/bin/python3
"""
This module defines the routes for the Flask app.
"""

from flask import Blueprint

# Create a Blueprint named 'main'
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Renders 'Hello HBNB!' on the root URL.
    """
    return 'Hello HBNB!'

