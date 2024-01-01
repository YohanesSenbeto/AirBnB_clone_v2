#!/usr/bin/python3
"""
This module initializes the Flask app.
"""

from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

<<<<<<< HEAD
# Configuration settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'b9e542897c0cdacb8b91558b4de734885d82710bb56cc292'

# Register blueprints
app.register_blueprint(main_blueprint)
=======
# Import routes (assuming you have a separate file for routes)
from web_flask import routes

>>>>>>> 89ae92d0a2f2a69379bfba508f80469f2ef3110c
