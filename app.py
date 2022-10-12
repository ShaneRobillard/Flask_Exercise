from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3h.
studentOrganisationDetails = ["John Smith","Brad Apple","Roger Tucker","Dominic Steve","Samanatha Carter"]

@app.get('/')
def index():
    now = datetime.datetime.now()
    currentDate = now.strftime("%d/%m/%Y %H:%M:%S")
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    global number
    number = request.form['number']
    if number.isnumeric() == False:
        calculate = "Not a number."
    elif int(number) % 2 == 0:
        calculate = "Number " + number + " is even!"
    elif int(number) % 2 != 0:
        calculate = "Number " + number + " is odd!"
    if len(number) == 0:
          calculate = "No number provided."  
        
    return render_template('result.html', calculate=calculate)

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')
    pass


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['student']
    studentOrganisationDetails.append(studentName)
    # Append this value to studentOrganisationDetails
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)
    # Display studentDetails.html with all students and organisations
