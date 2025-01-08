"""This creates a user in our database"""
from flask import Flask, jsonify


class User:
    """A class that takes user details for a database"""


    def signup(self):
        """Takes is user signin details"""
        user = {
            "id":"",
            "FullName":"",
            "username":"",
            "email":"",
            "password":""
        }

        return jsonify(user), 200
