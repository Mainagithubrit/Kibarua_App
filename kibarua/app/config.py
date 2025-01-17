"""This file configures flask"""
import os


class Config:
    """This class is used to configure my flask app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'app-kibarua-secrets'
