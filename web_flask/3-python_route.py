#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    new_text = text.replace("_", " ")
    return f"C {new_text}"


@app.route("/python/<text>", strict_slashes=False)
def Python_text(text):
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
