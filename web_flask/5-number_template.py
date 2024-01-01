#!/usr/bin/python3
"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    - /: Displays “Hello HBNB!”
    - /hbnb: Displays “HBNB”
    - /c/<text>: Displays “C ”, followed by the value of the text variable
      (replace underscore _ symbols with a space)
    - /python/(<text>): Displays “Python ”, followed by the text variable
      (replace underscore _ symbols with a space). The text is “is cool”
    - /number/<n>: Displays “n is a number” only if n is an integer
    - /number_template/<n>: Displays an HTML page only if n is an integer:
        - H1 tag: “Number: n” inside the tag BODY
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when accessing the root."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' when accessing /hbnb."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays 'C ' followed by the value of the text variable,
    replacing underscores _ symbols with a space.
    """
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Displays 'Python ' followed by the value of the text variable,
    replacing underscores _ symbols with a space. Default text is 'is cool'.
    """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays 'n is a number' only if n is an integer.
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page only if n is an integer.
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
