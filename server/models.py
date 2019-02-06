from app import db
from flask_login import UserMixin # does the db methods for you

class User(UserMixin, db.Model):
    """ User accounts """
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password