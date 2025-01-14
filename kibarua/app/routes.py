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
    if request.method == 'POST':
        users = mongo.db['users']
        username = request.form.get('username')
        password = request.form.get('passwrd')

        if not username or not password:
            return "Username and password are required", 400

        username_exists = users.find_one({'username': username})

        if (
                username_exists
                and bcrypt.checkpw(
                    password.encode('utf-8'),
                    username_exists['password']
                    )
            ):
            return redirect(url_for('choice'))
        return 'Invalid username, email and password', 400
    return render_template('login.html', title='Login Page', view='login')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    """This handles the sugnup route"""
    if request.method == 'POST':
        users = mongo.db['users']
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('passwrd')

        if not all([fullname, username, email, password]):
            return "All fields are required", 400
        
        user_exists = users.find_one({'username': username })

        if user_exists:
            return "Username already exists!", 400
            
        hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert_one({
            'fullname': fullname,
            'username': username,
            'email':email,
            'password': hashpass
            })
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign In Page', view='signup,')


@app.route('/choice')
def choice():
    """This handles the choice page for someone to choose whether to be
    a client or a skilled woker"""
    return render_template('choice.html')

if __name__ == "__main__":
    app.run(debug=True)
