import random

active_rooms = []
room_info = {}
possible_ans = ["dwight", "pam", "jim", "michael", "michael", "phillis"]


def room_creations():
    unique_id = random.randint(1000, 9999)
    while unique_id in active_rooms:
        unique_id = random.randint(1000, 9999)

    active_rooms.append(unique_id)
    ans1 = random.randint(0, 5)
    ans2 = random.randint(0, 5)
    while ans1 == ans2:
        ans2 = random.randint(0, 5)

    room_info[unique_id] = {'users': [], 'answers': [
        possible_ans[ans1], possible_ans[ans2]]}
    return unique_id


def get_room_info_and_join(room_id, username):
    room_id = int(room_id)

    if room_id not in active_rooms:
        return 'error'
    else:
        room_info[room_id]['users'].append(str(username))
        return room_info[room_id]


# def guess_answer(room_id, guess, username):
#     print(room_info)
#     ans_index = room_info[room_id]['users'].index(username)
#     if room_info[room_id]['answers'][ans_index] == guess:
#         return "Congrats you won"
#     else:
#         return "You lost"
#

'''
assuming that only 2 people join a game.
'''
