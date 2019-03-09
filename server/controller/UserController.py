from models import User
from app import bcrypt, db
def login_user_controller(username,password):
    user = User.query.filter_by(username=username).first()
    if user is not None and bcrypt.check_password_hash(user.password, password):
        return 'Success',user
    elif user is None:
        return "Username does not exist",user
    else:
        return "Wrong Password",user
def register_and_login_user_controller(email,username,password):
    if email and username and password:  # if its not empty lets say its valid
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username, email, password)
    else:
        return 'login failed! Something was empty',None

    if not User.query.filter_by(username=username).first() or not User.query.filter_by(email=email).first():
        db.session.add(new_user)
        db.session.commit()
        return 'Success', new_user
    return 'login failed! Username in use',None
