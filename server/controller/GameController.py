import random
import string

UNIQUE_ROOMS = []
ROOMS_STORE = {}


def create_unique_room_id():
    global UNIQUE_ROOMS
    while True:
        N = 4
        id = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=N))
        if id not in UNIQUE_ROOMS:
            UNIQUE_ROOMS.append(id)
            return id


def join_game_room(room, user):
    global ROOMS_STORE

    if room not in ROOMS_STORE:
        create_room(room, user)

    if user not in ROOMS_STORE[room]['listOfUsers']:
        ROOMS_STORE[room]["listOfUsers"].append(user)
        ROOMS_STORE[room]["userNotJudge"].append(user)


def create_room(room, user1, user2):
    ROOMS_STORE[room] = {
        list_of_users = [user1, user2]
    }

'''
def create_unique_room_id():
    global UNIQUE_ROOMS

    while True:
        N = 4
        id = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=N))
        if id not in UNIQUE_ROOMS:
            UNIQUE_ROOMS.append(id)
            return id

def create_room(room, user):
    global ROOMS_STORE

    gifs_available = giphy_api()

    # TODO: sending this data across all clients, needs improvement, only send client wants needed
    ROOMS_STORE[room] = {
        'question': '',
        'captain': user,
        'listOfUsers': [],
        'started': False,
        'judge': '',
        'availableGifs': gifs_available,
        'usedGifs': [],
        'round': 0,
        'userNotJudge': [],
        'userWasJudge': [],
        'gifPicks': {}
    }

def join_game_room(room, user):
    global ROOMS_STORE

    if room not in ROOMS_STORE:
        create_room(room, user)

    if user not in ROOMS_STORE[room]['listOfUsers']:
        ROOMS_STORE[room]["listOfUsers"].append(user)
        ROOMS_STORE[room]["userNotJudge"].append(user)

    return ROOMS_STORE[room]
