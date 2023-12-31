#!/usr/bin/python3
"""
This module initializes the Flask app.
"""

from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Import routes (assuming you have a separate file for routes)
from web_flask import routes

