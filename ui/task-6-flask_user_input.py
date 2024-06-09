#!/usr/bin/env python3

"""
Create a flask application for saying hello to a person
in random ways. The application should always show a text
input for a user to input a name, and a button labelled
‘Submit’.

When the submit button is pressed, the application displays
a salutation to the provided name. The salutation should be
randomly picked from the following list:

Hello
Hi
G’day
Greetings

As an example, when a user types in “Carla” into the text
box and presses the submit button, the application could
display “Greetings Carla”. If the user presses the button
again, the application could display “Hi Carla”, or any of
the other salutations including the already displayed
salutation.
"""

from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of possible salutations
salutations = ["Hello", "Hi", "G’day", "Greetings"]

@app.route('/')
def index():
    return render_template('task6.html')

@app.route('/', methods=['POST'])
def greet():
    name = request.form['name']
    salutation = random.choice(salutations)
    return render_template('task6.html', name=name, salutation=salutation)

if __name__ == '__main__':
    app.run(debug=True)
