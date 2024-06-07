import random
from brain_games.constants import MAX_ATTEMPTS
from brain_games.game_logic import (
    print_correct_answer,
    print_question,
    print_user_lose,
    print_wrong_answer,
    get_user_answer_string,
    print_user_win
)
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def is_prime_number(number: int):
    if number < 2:
        return 'no'

    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1

    return 'yes'


def handle_game_round(name: str) -> bool:
    prime_number = random.randint(1, 100)
    print_question(prime_number)

    user_answer = get_user_answer_string()
    correct_answer = is_prime_number(prime_number)

    if user_answer == correct_answer:
        print_correct_answer()
        return True
    else:
        print_wrong_answer(user_answer, correct_answer)
        return False


def brain_prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

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
    brain_prime_game(name)


if __name__ == '__main__':
    main()
