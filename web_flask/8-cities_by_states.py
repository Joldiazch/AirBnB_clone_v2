#!/usr/bin/python3
""" that starts a Flask web application """
# import flask
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_of_states():
    states = storage.all(State).values()
    return render_template(
        '8-cities_by_states.html',
        states=states,
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
