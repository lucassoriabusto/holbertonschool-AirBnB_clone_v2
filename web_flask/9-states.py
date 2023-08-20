#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template
import models
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    stateslist = models.storage.all(State).values()
    return render_template("9-states.html", stateslist=stateslist)


@app.route("/states/<id>", strict_slashes=False)
def list_states_id(id):
    stateslist = models.storage.all(State).values()
    found_states = []
    for state in stateslist:
        if state.id == id:
            found_states.append(state)
    return render_template("9-states.html", stateslist=stateslist,
                           found_states=found_states, id=id)


@app.teardown_appcontext
def teardown(self):
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
