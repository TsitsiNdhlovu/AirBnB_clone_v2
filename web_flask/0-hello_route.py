#!/usr/bin/python3
'''It is a simple Flask web application.
'''
from flask import Flask


app = Flask(__name__)
'''The Flask application instance.'''
@app.route('/airbnb-onepage/', strict_slashes = False)

def hello_hbnb():
    '''The home page.'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
