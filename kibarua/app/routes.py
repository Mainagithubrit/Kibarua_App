"""This handles the routes for the app"""
from flask import render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
from . import mongo, mail
import bcrypt
from flask_mail import Message
from .config_passwrd import Email, password
from flask import flash

def register_routes(app):
    @app.route('/')
    @app.route('/index', methods=['GET', 'POST'])
    def index():
        """This handles the Home route and sends an email"""
        if request.method == "POST":
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')

            if not name or not email or not message:
                flash("All fields are required", "error")
                return render_template('index.html', title='Home')

            msg = Message(subject=f"Mail from: {name}",
                          body=f"""
                          Name: {name}\n
                          E-mail: {email}\n\n\n
                          Message: {message}""",
                          sender=Email,
                          recipients=["njorogefrancismaina@gmail.com"])
            mail.send(msg)
            return render_template('index.html', success=True)
        return render_template('index.html', title='Home')

    @app.route('/login', methods=["GET", 'POST'])
    def login():
        """This handles the login route"""
        if request.method == 'POST':
            users = mongo.db['users']
            username = request.form.get('username')
            password = request.form.get('passwrd')

            if not username or not password:
                flash("Username and password are required", "error")
                return render_template('login.html', title='Login Page', view='login')

            username_exists = users.find_one({'username': username})

            if (
                username_exists
                and bcrypt.checkpw(
                    password.encode('utf-8'),
                    username_exists['password']
                )
            ):
                session['username'] = username
                return redirect(url_for('choice'))
            flash('Invalid username or password', "error")
            return render_template('login.html', title='Login Page', view='login')

        return render_template('login.html', title='Login Page', view='login')

    @app.route('/signup', methods=('GET', 'POST'))
    def signup():
        """This handles the signup route"""
        if request.method == 'POST':
            users = mongo.db['users']
            fullname = request.form.get('fullname')
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('passwrd')

            if not all([fullname, username, email, password]):
                flash("All fields are required", "error")
                return render_template('signup.html', title='Sign In Page', view='signup')

            user_exists = users.find_one({'username': username})

            if user_exists:
                flash("Username already exists!", "error")
                return render_template('signup.html', title='Sign In Page', view='signup')

            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users.insert_one({
                'fullname': fullname,
                'username': username,
                'email': email,
                'password': hashpass
            })
            return redirect(url_for('login'))
        return render_template('signup.html', title='Sign In Page', view='signup')

    @app.route("/choice")
    def choice():
        """This handles the choice page for someone to choose whether to be
        a client or a skilled worker"""
        if 'username' not in session:
            return redirect(url_for('login'))
        return render_template('choice.html', title='Choice', view='choice')

    if __name__ == "__main__":
        app.run(debug=True)
