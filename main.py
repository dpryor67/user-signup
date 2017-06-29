from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('edit.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password = ''
    email_error = ''



@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html', name=username)

app.run()
