#!/usr/bin/python3
""" Script that start a flask app with two routes """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ prints Hhello """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ Prints C with a text followed """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
