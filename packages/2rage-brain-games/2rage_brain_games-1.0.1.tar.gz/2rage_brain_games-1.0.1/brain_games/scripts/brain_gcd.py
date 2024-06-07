import random
from brain_games.constants import MAX_ATTEMPTS
from brain_games.game_logic import (
    get_user_answer_integer,
    print_question,
    print_correct_answer,
    print_user_lose,
    print_user_win,
    print_wrong_answer,
)

from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user


def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    for i in range(num2, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


def handle_game_round(name):
    random_number1 = random.randint(1, 12)
    random_number2 = random.randint(1, 12)
    print_question(random_number1, random_number2)

    user_answer = get_user_answer_integer()
    right_answer = gcd(random_number1, random_number2)

    if user_answer == right_answer:
        print_correct_answer()
        return True
    else:
        print_wrong_answer(user_answer, right_answer)
        return False


def brain_greatest_common_divisor(name):
    print('Find the greatest common divisor of given numbers.')

    round_played = 0

    while round_played < MAX_ATTEMPTS:
        if handle_game_round(name):
            round_played += 1
        else:
            print_user_lose(name)
            break

    if round_played == MAX_ATTEMPTS:
        print_user_win(name)


def main():
    greet()
    name = welcome_user()
    brain_greatest_common_divisor(name)


if __name__ == "__main__":
    main()
