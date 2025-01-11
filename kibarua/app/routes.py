"""This handles the routes for the app"""
from flask import render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from . import app, mongo
import bcrypt


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
    if request.method == 'POST':
        users = mongo.db['users']
        user_exists = users.find_one({'name': request.form['username']})

        if user_exists is None:
            hashpass = bcrypt.hashpw(request.form['passwrd'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'fullname': request.form['fullname'],
                'username': request.form['username'],
                'email': request.form['email'], 'password': hashpass})
            return redirect(url_for('login'))
        return 'That username already exists!'
    return render_template('signup.html', title='Sign In Page', view='signup,')

if __name__ == "__main__":
    app.run(debug=True)
