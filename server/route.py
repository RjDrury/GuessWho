from app import app,db,bcrypt,login_manager, socketio
from flask import render_template, request, redirect, session
from models import *
from flask_login import login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, send, emit
from controller.UserController import login_user_controller,register_and_login_user_controller
from controller.RelationshipController import add_friend_controller, get_friends_list
@app.route('/')
def hello_world():
    #return render_template('index.html', logged_in=True, user=username)
    if not current_user.is_authenticated:
        return redirect('/signup')

    #user = session.get('username')
    get_friends_list(current_user)
    return render_template('home.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@app.route('/signup')
def signup_page():
    return render_template("signup.html")

@app.route('/signup', methods=['POST'])
def sign_up():
    email = request.form.get('email_register')
    username = request.form.get('username_register')
    password = request.form.get('password_register')

    error_msg, user = register_and_login_user_controller(email,username,password)
    if user is not None:
        login_user(user)
        return redirect('/')
    else:
        print(error_msg)
        return redirect('/signup')

#Login to server
@app.route('/login', methods=['POST'])
def verify_login():
    username = request.form.get('username')
    testPassword = request.form.get('password')

    error_login_message, user = login_user_controller(username,testPassword)

    if user is not None:
        login_user(user)
        return redirect("/")
    else:
        print(error_login_message)
        return render_template("signup.html", logged_in=False)

@app.route('/logout')
@login_required
def logout():
    print(current_user.username)
    logout_user()
    return redirect("/")

@app.route('/addfriend', methods=['POST'])
@login_required
def add_friend():
    this_username = current_user.username
    friend_to_add = request.form.get('friend_to_add')
    print(add_friend_controller(this_username,friend_to_add))
    return redirect("/")

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
    
@socketio.on('connect')
def test_connect():
    send('User has connected', broadcast=True)