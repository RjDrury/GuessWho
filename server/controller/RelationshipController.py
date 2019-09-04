from models import UserRelationships, User
from app import db


def proper_id_order(id1, id2):
    greater_id = 0
    less_id = 0
    if id1 == id2:
        return 'cannot do dat shit'
    elif id1 < id2:
        greater_id = id1
        less_id = id2
    else:
        greater_id = id2
        less_id = id1
    print(greater_id, less_id)
    return greater_id, less_id


def get_User_from_username(username):
    user = User.query.filter_by(username=username).first()
    return user


def get_relationship_list(User):
    friends_list = []
    blocked_list = []
    pending_list = []

    current_users_relationships = UserRelationships.query.filter_by(
        id_1=User.id).all()

    for rel in current_users_relationships:
        if rel.relationship == 'friends':
            friends_list.append(User.query.filter_by(
                id=rel.id_2).first().username)
        elif 'pending' in rel.relationship:
            pending_list.append(User.query.filter_by(
                id=rel.id_2).first().username)
        else:
            blocked_list.append(User.query.filter_by(
                id=rel.id_2).first().username)

    current_users_relationships = UserRelationships.query.filter_by(
        id_2=User.id).all()

    for rel in current_users_relationships:
        if rel.relationship == 'friends':
            friends_list.append(User.query.filter_by(
                id=rel.id_1).first().username)
        elif 'pending' in rel.relationship:
            pending_list.append(User.query.filter_by(
                id=rel.id_1).first().username)
        else:
            blocked_list.append(User.query.filter_by(
                id=rel.id_1).first().username)
    return friends_list, blocked_list, pending_list


def add_friend_controller(username_current_user, username_to_add):
    user_current_user = get_User_from_username(username_current_user)
    user_to_add = get_User_from_username(username_to_add)  # get user objects
    if user_current_user is not None and user_to_add is not None:
        small_id, big_id = proper_id_order(
            user_current_user.id, user_to_add.id)
        if small_id == big_id:
            return 'Fail, not able to add yourself'
        relationship = UserRelationships.query.filter_by(id_1=small_id).all()

        users_have_rel = False
        for rel in relationship:
            if rel.id_2 == big_id:
                # if user already tried to add
                if rel.relationship == (str(user_current_user.id)+' pending '+str(user_to_add.id)):
                    return 'failed, friend request already pending'
                elif rel.relationship == (str(user_to_add.id)+' pending '+str(user_current_user.id)):
                    db.session.delete(rel)
                    db.session.commit()
                    new_rel = UserRelationships(small_id, big_id, 'friends')
                    db.session.add(new_rel)
                    db.session.commit()
                    return 'users are now friends'
                elif rel.relationship == 'friends':
                    return 'users are already friends'
                users_have_rel = True
        if not users_have_rel:
            new_rel = UserRelationships(small_id, big_id, str(
                user_current_user.id)+' pending '+str(user_to_add.id))
            db.session.add(new_rel)
            db.session.commit()
            return 'Pending friend request sent'


def block_friend_controller(username_current_user, username_to_add):
    user_current_user = get_User_from_username(username_current_user)
    user_to_add = get_User_from_username(username_to_add)  # get user objects
    if user_current_user is not None and user_to_add is not None:
        small_id, big_id = proper_id_order(
            user_current_user.id, user_to_add.id)
        if small_id == big_id:
            return 'Fail, not able to add yourself'
        relationship = UserRelationships.query.filter_by(id_1=small_id).all()

        users_have_rel = False
        for rel in relationship:
            if rel.id_2 == big_id:
                if blocked not in rel.relationship:
                    db.session.delete(rel)
                    db.session.commit()
                    new_rel = UserRelationships(small_id, big_id, str(
                        user_current_user.id)+' blocked '+str(user_to_add.id))
                    db.session.add(new_rel)
                    db.session.commit()
                    return 'user is blocked'
                elif rel.relationship == (small_id, big_id, str(user_current_user.id)+' blocked '+str(user_to_add.id)):
                    return 'User was already blocked'
                else:
                    db.session.delete(rel)
                    db.session.commit()
                    new_rel = UserRelationships(small_id, big_id, 'blocked')
                    db.session.add(new_rel)
                    db.session.commit()
                    return 'User is blocked'

        if not users_have_rel:
            new_rel = UserRelationships(small_id, big_id, str(
                user_current_user.id)+' blocked '+str(user_to_add.id))
            db.session.add(new_rel)
            db.session.commit()
            return 'User is blocked'
