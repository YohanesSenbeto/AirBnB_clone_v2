#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display an HTML page like 8-index.html."""
    # Copy necessary files to the specified folders
    # You can use Flask's `send_from_directory` to serve static files
    # Fetch data from storage engine (DBStorage or FileStorage)
    # Load State, City, Amenity, and Place objects sorted by name
    # Render the template with the fetched data
    return render_template('100-hbnb.html', data=data_from_storage)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
