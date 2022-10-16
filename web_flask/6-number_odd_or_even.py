#!/usr/bin/python3
""" Script that start a flask app with two routes """
from flask import Flask
from flask import render_template
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
    """ Prints python with default text """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Prints the number passed as argument """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Displays an html page"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_odd(n):
    """ Displays an HTML of odd or even """
    if (n %2 == 0):
        t_pe = 'even'
    else:
        t_pe = 'odd'
    return render_template("6-number_odd_or_even.html", n=n, t_pe=t_pe)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
