#!/usr/bin/python3
""" that starts a Flask web application """
# import flask
from flask import Flask, render_template


app = Flask(__name__)
# strict_slashes allow that this route work with /my_route and /my_route/
@app.route('/', strict_slashes=False)
def root():
    """ return Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_int_template(n):
    return render_template(
        '5-number.html',
        number=n
    )


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    type_num = {'1': 'odd', '0': 'even'}
    msg = '{} is {}'.format(n, type_num[str(n % 2)])
    return render_template(
        '6-number_odd_or_even.html',
        msg=msg
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)
