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


@app.route('/hbnb_filters')
def hbnb_filters():
    """hbnb_filters method"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
