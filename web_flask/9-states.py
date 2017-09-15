#!/usr/bin/python3
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """calls close method of storage"""
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def state_id(id=None):
    """state_id method"""
    if id is None:
        states = storage.all("State")
        return render_template('7-states_list.html', states=states)
    state_id = str(id)
    states = storage.all("State").values()
    for state in states:
        if state.id == state_id:
            state_name = state.name
            cities = state.cities
            return render_template('9-states.html', condition='found',
                                   state_name=state_name, cities=cities)
    return render_template('9-states.html', condition='not_found')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
