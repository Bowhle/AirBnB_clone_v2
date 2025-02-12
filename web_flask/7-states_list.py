#!/usr/bin/python3
"""a script that starts a flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function prints hello hbnb at the root"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """THis function displays HBNB at /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """This functions displays “C” followed by the value
    of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """This functions displays python followed by the value of the text
    variable and replaces _ with space"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This function displays n if it's an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """This function displays a html page with template"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ This function displays n only if it's an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

@app.teardown_appcontext
def teardown(exc):
    """Closes the SQLAlchemy session after each request."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all states sorted by name."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    # Render a template to display the states
    return render_template("7-states_list.html", states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
