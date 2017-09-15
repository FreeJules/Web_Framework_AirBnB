#!/usr/bin/python3
from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """number_template method"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
