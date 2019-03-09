from app import db
from flask_login import UserMixin # does the db methods for you expected by flask login

class User(UserMixin, db.Model):
    """ User accounts """
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    facebook_apikey= db.Column(db.String(128))
    
    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
class UserRelationships(db.Model):
    'table defining user relationships, id_1 must be < id_2'

    id_1 = db.Column(db.Integer, primary_key=True)
    id_2 = db.Column(db.Integer)
    relationship = db.Column(db.String(30), nullable = False)
    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, id_1,id_2, relationship):
        self.id_1 = id_1
        self.id_2 = id_2
        self.relationship = relationship