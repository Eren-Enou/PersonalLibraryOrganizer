# File: app/__init__.py

from flask import Flask
from flask_login import LoginManager

from .config import Config

from app.database import db

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
#     db.init_app(app)

#     with app.app_context():
#         db.create_all()

#     # Import models and routes after db initialization
#     from app.models import title, user  # Adjust imports as needed

#     return app

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Specify the view that handles logins

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Import routes here
from app.models import User
from app import routes

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_tables():
    with app.app_context():
        db.create_all()
    
from app.models import User, Title

# create_tables() #Run if new tables are created.