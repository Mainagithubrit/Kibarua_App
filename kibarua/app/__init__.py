"""This starts a flask and a mongodb connection"""

from flask import Flask
from flask_pymongo import PyMongo
from flask_mail import Mail
from .config_passwrd import Email, password
from .config import Config
mongo = PyMongo()
mail = Mail()


def create_app():
    """a funtion that creates my app"""
    app = Flask(__name__)
    app.config['MONGO_URI'] = "mongodb://localhost:27017/kibarua_db"

    app.config.from_object(Config)

    app.config['MAIL_SERVER']= "smtp.gmail.com"
    app.config['MAIL_PORT']= 465
    app.config['MAIL_USERNAME'] = Email
    app.config['MAIL_PASSWORD'] = password
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] =True

    mongo.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from .routes import register_routes
        register_routes(app)
    return app
