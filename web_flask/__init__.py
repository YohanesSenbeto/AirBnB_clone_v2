#!/usr/bin/python3
from web_flask import routes
from flask import Flask
"""
This module initializes the Flask app.
"""

# Create the Flask app instance
app = Flask(__name__)
<<<<<<< HEAD
=======

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
>>>>>>> 68a238db4b9730d7443e68db7ad84a8a07b78e36
