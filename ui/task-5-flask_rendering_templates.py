#!/usr/bin/env python3

"""
Create a flask application that makes use of a rendering
template to wish a user hello and tell them the current
date in Brisbane Australia.

Similar to the HTML Escaping task, the application should
make use of a variable under a route “/person/” that should
provide the name for a person. That name should then be used
along with a rendering template to display “Hello {name},
today’s date is {date in Brisbane yyyy-mm-dd}.” The text
should be H1 sized.

As an example, when passed “/person/James” and if the current
date in Brisbane is the 12th of June 2024, the webpage would
display “Hello James, today’s date is 2024-06-12.
"""

from flask import Flask, render_template
from datetime import datetime, timedelta
from pytz import timezone

app = Flask(__name__)

# Define a function to get the current date in Brisbane
def get_brisbane_date():
    brisbane = timezone('Australia/Brisbane')
    brisbane_time = datetime.now(brisbane)
    return brisbane_time.strftime('%Y-%m-%d')

@app.route('/person/<name>')
def hello_person(name):
    date = get_brisbane_date()
    return render_template('hello.html', name=name, date=date)

if __name__ == '__main__':
    app.run(debug=True)
