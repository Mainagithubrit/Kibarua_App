"""This handles the routes for the app"""
from flask import render_template, request, url_for, redirect
from pymongo import MongoClient
from app import app

app.config['STRICT_SLASHES'] = False

@app.route('/')
@app.route('/index')
def index():
    """This handles the Home route"""
    return render_template('index.html', title='Home')

@app.route('/login', methods=["GET"])
def login():
    """This handles the login route"""
    return render_template('login.html', title='Login Page', view='login')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    """This handles the sugnup route"""
    return render_template('signup.html', title='Sign In Page', view='signup')

if __name__ == "main":
    app.run(debug=True)
