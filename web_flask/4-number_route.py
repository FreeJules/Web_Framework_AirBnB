#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """hello method"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """hbnb method"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text="is cool"):
    """C method"""
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


@app.route('/python')
@app.route('/python/<text>')
def python_is(text="is cool"):
    """pyhton method"""
    text = text.replace('_', ' ')
    return ('Python {}'.format(text))


@app.route('/number/<int:n>')
def number_is(n):
    """number method"""
    return ('{} is a number'.format(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
