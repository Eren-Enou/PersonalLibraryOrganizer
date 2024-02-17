import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'a_very_secret_key'
    DEBUG = True  
    SESSION_TYPE = 'filesystem'  # For storing sessions on the file system
    SERVER_NAME = 'localhost:5000'


