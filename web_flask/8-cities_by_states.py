#!/usr/bin/python3
"""Script that starts a flask web application and displays states with their cities"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exc):
    """Closes the SQLAlchemy session after each request."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a list of all states and their cities sorted by name."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    # Create a list of states with their cities
    states_and_cities = []
    for state in sorted_states:
        if hasattr(state, 'cities'):  # DBStorage: check if cities relationship exists
            cities = sorted(state.cities, key=lambda city: city.name)  # Sort cities by name
        else:  # FileStorage: use the public getter method
            cities = sorted(state.cities(), key=lambda city: city.name)

        states_and_cities.append({
            'state': state,
            'cities': cities
        })

    # Render the template to display states and their cities
    return render_template("8-cities_by_states.html", states_and_cities=states_and_cities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
