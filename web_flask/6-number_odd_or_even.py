#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask
from flask import render_template


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
@app.route("/python/", strict_slashes=False)
def Python_text(text="is cool"):
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    return render_template("6-number_odd_or_even.html", n=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
