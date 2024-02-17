from app.database import db

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    status = db.Column(db.String(20))
    link = db.Column(db.String(255))  # For storing a URL

    def __repr__(self):
        return f'<Title {self.name}>'
