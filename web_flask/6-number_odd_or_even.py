#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
=======
"""A script that starts a Flask web application
"""
>>>>>>> 622eaf7cee9a5e80fa124a9d76f2ced08e9b2a4d
from flask import Flask, render_template


app = Flask(__name__)
<<<<<<< HEAD
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python')
def python_page(text='is cool'):
    '''The python page.'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''The number page.'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''The number_template page.'''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''The number_odd_or_even page.'''
    ctxt = {
        'n': n
    }
    return render_template('6-number_odd_or_even.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def holberon():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}" .format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function called with /python/<text> route """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ display a HTML page only if n is an integer """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_html_odd_even(n):
    """ display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 622eaf7cee9a5e80fa124a9d76f2ced08e9b2a4d
