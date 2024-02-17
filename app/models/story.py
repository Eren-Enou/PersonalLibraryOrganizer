# File: app/models/story.py

from app.database import db

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(128))
    description = db.Column(db.Text)
    # Add more fields as necessary
