#!/usr/bin/python3
""" that starts a Flask web application """
# import flask
from flask import Flask


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
