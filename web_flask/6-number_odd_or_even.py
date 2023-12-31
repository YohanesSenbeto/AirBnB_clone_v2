#!/usr/bin/python3
"""
A Flask web application.

Listens on 0.0.0.0, port 5000.
Routes:
    - /: Displays “Hello HBNB!”
    - /hbnb: Displays “HBNB”
    - /c/<text>: Displays “C ”, followed by the value of the text variable
      (replacing underscores with spaces)
    - /python/(<text>): Displays “Python ”, followed by the value
    (replacing underscores with spaces). Default text is “is cool”
    - /number/<n>: Displays “n is a number” only if n is an integer
    - /number_template/<n>: Displays an HTML page only if n is an integer:
        - H1 tag: “Number: n” inside the BODY tag
        - Appends even or odd info to the H1 tag based on n
    - /number_odd_or_even/<n>: Displays an HTML page only if n is an integer:
        - H1 tag: “Number: n is even|odd” inside the BODY tag
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' at the root."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' at /hbnb."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays 'C ' followed by text, replacing underscores with spaces."""
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Displays 'Python ' followed by text, replacing underscores with spaces.
    Default text is 'is cool'.
    """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' only if n is an integer."""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page only if n is an integer.
    Adds even or odd info to the H1 tag based on n.
    """
    num_type = 'even' if n % 2 == 0 else 'odd'
    return render_template('5-number.html', num=n, num_type=num_type)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page only if n is an integer.
    Adds info about n being odd or even to the H1 tag.
    """
    num_type = 'even' if n % 2 == 0 else 'odd'
    a = num = n
    b = num_type = num_type
    return render_template('6-number_odd_or_even.html', a, b)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
