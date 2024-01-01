#!/usr/bin/python3

"""
Module: 0-gather_data_from_an_API
Script to gather data from an API and export to a JSON file
"""

from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)


def teardown_db(exception):
    """
    Function to close the database connection after each request
    """
    storage.close()


@app.teardown_appcontext
def teardown_db(exception):
    """
    Function to close the database connection after each request
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Route to display cities by states
    Retrieves all State objects from the database, sorts them by name,
    and renders a template with the sorted states.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
