import random

active_rooms = []
room_info = {}


def room_creations():
    unique_id = random.randint(1000, 9999)
    while unique_id in active_rooms:
        unique_id = random.randint(1000, 9999)

    active_rooms.append(unique_id)
    room_info[unique_id] = {'users': [], 'score': ''}
    return unique_id


def get_room_info_and_join(room_id, username):
    room_id = int(room_id)

    if room_id not in active_rooms:
        return 'error'
    else:
        print(room_info)
        room_info[room_id]['users'].append(username)
        return room_info[room_id]
