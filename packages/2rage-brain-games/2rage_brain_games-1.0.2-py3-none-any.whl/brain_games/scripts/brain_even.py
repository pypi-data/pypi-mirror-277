import random
import prompt
from brain_games.constants import MAX_ATTEMPTS
from brain_games.game_logic import (
    print_correct_answer,
    print_user_lose,
    print_user_win,
    print_wrong_answer,
)

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def handle_game_round(name) -> bool:
    random_number = random.randrange(1, 99)
    print(f'Question: {random_number}')

    correct_answer = is_even(random_number)
    user_answer = prompt.string('Your answer: ')

    if user_answer != 'yes' and user_answer != 'no':
        print('Error. Please enter answer "yes" or "no"')
        return False

    if correct_answer == user_answer:
        print_correct_answer()
        return True
    else:
        print_wrong_answer(user_answer, correct_answer)
        return False


def brain_even_number(name) -> int:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds_played = 0

    while rounds_played < MAX_ATTEMPTS:
        if handle_game_round(name):
            rounds_played += 1
        else:
            print_user_lose(name)
            break

    if rounds_played == MAX_ATTEMPTS:
        print_user_win(name)


def main():
    greet()
    name = welcome_user()
    brain_even_number(name)


if __name__ == '__main__':
    main()
