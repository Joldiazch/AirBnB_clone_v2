#!/usr/bin/python3
""" hello world with flask framework """
# import flask
from flask import Flask


app = Flask(__name__)
# strict_slashes allow that this route work with /my_route and /my_route/


@app.route('/', strict_slashes=False)
def my_function():
    """ return Hello HBNB """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
