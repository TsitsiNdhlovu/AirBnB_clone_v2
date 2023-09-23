#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
=======
"""A script that starts a Flask web application
"""
>>>>>>> 622eaf7cee9a5e80fa124a9d76f2ced08e9b2a4d
from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def holberon():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 622eaf7cee9a5e80fa124a9d76f2ced08e9b2a4d
