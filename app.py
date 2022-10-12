from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3h.


@app.get('/')
def index():
    now = datetime.now()
    currentDate = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    return render_template('form.html')
    pass


@app.route('/calculate', methods=['POST'])
def checkNumber():
    global number
    number = request.form['number']
    if request.method == "POST":
        number = request.form.get("number")
        if int(number) % 2 == 0:
            return f'{number} is even. <br><a href = "/">Go home</a>'
        elif int(number) % 2 != 0:
            return f'{number} is odd. <br><a href = "/">Go home</a>'
        elif not number:
            return 'No number provided. <br><a href = "/">Go home</a>'
        else:
            return 'Provided input is not an integer! <br><a href = "/">Go home</a>'

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    pass


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']

    # Append this value to studentOrganisationDetails

    # Display studentDetails.html with all students and organisations
