#!/usr/bin/python3
"""
This module initializes the Flask app.
"""
from flask import Blueprint, Flask


# Create the Flask app instance
app = Flask(__name__)

# Create a blueprint
main_blueprint = Blueprint('main', __name__)


# Define routes within the blueprint
@main_blueprint.route('/')
def hello():
    return 'Hello HBNB!'


@main_blueprint.route('/hbnb')
def hbnb():
    return 'HBNB'

# Register the blueprint with the Flask app
app.register_blueprint(main_blueprint, url_prefix='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
