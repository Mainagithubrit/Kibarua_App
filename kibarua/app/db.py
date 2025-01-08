"""This program creates a connection between the app and MongoDB"""
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.kibarua_db
username_collection = db.username
