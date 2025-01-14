"""This starts a flask and a mongodb connection"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/kibarua_db"
mongo = PyMongo(app)

from . import routes
