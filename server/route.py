from app import app,db,bcrypt,login_manager, socketio
from flask import render_template, request, redirect, session
from models import User
from flask_login import login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, send, emit

@app.route('/')
def hello_world():
    #return render_template('index.html', logged_in=True, user=username)
    if not current_user.is_authenticated:
        return redirect('/signup')

    #user = session.get('username')
    print(current_user.username)
    return render_template('home.html')

@login_manager.user_loader
def load_user(user_id):
    lol = User.query.filter_by(id=user_id).first()
    return lol

@app.route('/signup')
def signup_page():
    return render_template("signup.html")

@app.route('/signup', methods=['POST'])
def sign_up():

    email = request.form.get('email_register')
    username = request.form.get('username_register')
    password = request.form.get('password_register')

    if email and username and password:  # if its not empty lets say its valid
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username, email, password)
        # see if the name  or email is in use
        if not User.query.filter_by(username=username).first() or not User.query.filter_by(email=email).first():
            db.session.add(new_user)
            db.session.commit()
    return redirect('/')

#Login to server
@app.route('/login', methods=['POST'])
def verify_login():

    username = request.form.get('username')
    testPassword = request.form.get('password')
    user = User.query.filter_by(username=username).first()

    if user is not None and bcrypt.check_password_hash(user.password, testPassword):
        login_user(user)
        #session['username'] = username
        return redirect("/")
    else:
        return render_template("signup.html", logged_in=False)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
    
@socketio.on('connect')
def test_connect():
    send('my response', broadcast=True)