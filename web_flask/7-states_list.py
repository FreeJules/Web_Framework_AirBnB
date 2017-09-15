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


@app.route('/states_list')
def states_list():
    """states_list method"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
