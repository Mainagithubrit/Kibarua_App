from flask import Flask
import db

app = Flask(__name__)

from app import routes
from pymongo import MongoClient
