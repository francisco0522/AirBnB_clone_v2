#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    textC = text.replace('_', ' ')
    return 'C {}'.format(textC)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    textC = text.replace('_', ' ')
    return 'Python {}'.format(textC)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
