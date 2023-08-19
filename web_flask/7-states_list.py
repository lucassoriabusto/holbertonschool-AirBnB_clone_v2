#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)

    """ Cerrar la sesión de SQLAlchemy después de cada solicitud """
    @app.teardown_appcontext
    def teardown_db(exception):
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)