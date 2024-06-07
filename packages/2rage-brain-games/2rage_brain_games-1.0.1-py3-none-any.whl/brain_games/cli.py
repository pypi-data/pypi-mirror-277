#!/usr/bin/env python3

import prompt
from brain_games.constants import MAX_NAME_LENGTH


def welcome_user():
    while True:
        name = prompt.string('May I have your name? ')
        if len(name) < MAX_NAME_LENGTH:
            print('Your name must be at least 4 characters long.')
        elif name.isdigit():
            print('Your name cannot Consist only of digits. Please try again.')
        else:
            break

    print(f'Hello, {name}')
    return name
