from flask import Flask
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5433/guesswho_dev'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
socketio = SocketIO(app)
from route import *

if __name__ == '__main__':
    app.secret_key = "top_secret"
    db.create_all()
    socketio.run(app)