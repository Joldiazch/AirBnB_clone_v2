#!/usr/bin/python3
""" that starts a Flask web application """
# import flask
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_of_states():
    states = storage.all(State).values()
    list_states = [{'name': state.name, 'id': state.id} for state in states]
    list_states = sorted(list_states, key=lambda i: i['name'])
    return render_template(
        '7-states_list.html',
        states=list_states
    )


@app.teardown_appcontext
def teardown_db():
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
