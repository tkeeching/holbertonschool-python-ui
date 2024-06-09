#!/usr/bin/env python3

"""
Create a Flask application with a url variable under the
route “/person/” called <first_name>.

Have your Flask application return ‘Hello {first_name}’
inside of a html <H1> tag when someone navigates to a name
under the /person/ route. E.g. navigating to …/person/Bob
would display a webpage with a H1 header of ‘Hello Bob’.

Appropriately escape the <first_name> variable to protect
against injection attacks to your Flask Application.
"""

from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)

@app.route('/person/<first_name>')
def hello_person(first_name):
    return f'<h1>Hello {escape(first_name)}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
