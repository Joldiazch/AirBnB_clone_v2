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


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def list_of_states(id=None):
    states = storage.all(State).values()
    list_ids = [state.id for state in states]
    if id in list_ids:
        states = [state for state in states if state.id == id]
    elif id != None:
        id = 'Not found'
    return render_template(
        '9-states.html',
        states=states,
        id=id,
        ids=list_ids,
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
