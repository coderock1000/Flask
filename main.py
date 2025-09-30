from flask import Flask, render_template,request
from datatime import datetime
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def calculate_age():
    try :
        birthyear = int(request.form['birthyear'])
        current_year = datetime.now().year
        if birthyear > current_year or birthyear < 1900:
            return render_template('index.html', error="Please enter a valid year between 1900 and the current year.")
        age = current_year - birthyear

    