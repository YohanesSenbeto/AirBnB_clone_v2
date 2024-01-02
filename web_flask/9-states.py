#!/usr/bin/python3
"""The Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a list of states"""
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def display_state_cities(state_id):
    """Display cities of a specific state"""
    state = storage.get("State", state_id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', cities=cities, state=state)
    return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
