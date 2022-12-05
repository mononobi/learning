"""
This is a self practice, not exactly a homework. I want to use json to build some utilities.
I want to retain the names of people who have run this python file. ask for their names and store it in a file.
On each new run I will give a report.
"""

import json

filepath = 'd:/Python/user_info.json'

info_types = ('name', 'age', 'city')


def show_user_stats():
    """ Check for log file of previous users and show some stats"""

    try:
        with open(filepath) as file:
            global users_info
            users_info = json.load(file)
        print(f'Up to now, we had {len(users_info)} users.')

    except FileNotFoundError:
        print('You are our first user!')


def store_new_user():
    """"asks for info of new user and stores it if name is not repetitive"""

    # A flag to check if it is ok to store the name
    store_info = True
    new_user_info = dict()

    # store lower case user names to avoid repetition.
    names = []
    for user in users_info:
        names.append(user['name'].lower())

    for info in info_types:
        new_user_info[info] = input(f'What is your {info}? ')
        if new_user_info['name'].lower() in names:
            print('Already registered. Remember that names are case sensitive.')
            store_info = False
            break

    if store_info:
        users_info.append(new_user_info)

    with open(filepath, 'w') as file:
        json.dump(users_info, file)


while 1:
    show_user_stats()
    store_new_user()
    continue_char = input('If you want to store another user, press "y"?')
    if continue_char != 'y' and continue_char != 'Y':
        break
