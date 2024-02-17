# File: app/models/manga.py

from app.database import db

class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mangadex_id = db.Column(db.String(128), unique=True, nullable=False)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    # Add more fields as necessary
