#!/usr/bin/python3
"""
This module initializes the Flask app.
"""

from flask import Flask
from .routes.routes import main_blueprint

app = Flask(__name__)

# Configuration settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'b9e542897c0cdacb8b91558b4de734885d82710bb56cc292'

# Register blueprints
app.register_blueprint(main_blueprint)

