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


def math_addition(number1, number2) -> int:
    return number1 + number2


def math_subtraction(number1, number2) -> int:
    return number1 - number2


def math_multiplication(number1, number2) -> int:
    return number1 * number2


def math_division(number1, number2) -> int:
    return number1 // number2


def generate_expression() -> tuple[int, str, int]:
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    num1, num2 = max(num1, num2), min(num1, num2)  # Ensure num1 >= num2
    operator = random.choice(['+', '-', '*'])
    return num1, operator, num2


def calculate_result(a: int, operator: str, b: int) -> int:
    operations = {
        '+': math_addition,
        '-': math_subtraction,
        '*': math_multiplication,
        '/': math_division
    }
    return operations[operator](a, b)


def handle_game_round(name: str) -> bool:
    a, operator, b = generate_expression()
    print_question(a, operator, b)

    user_answer = get_user_answer_integer()
    correct_answer = calculate_result(a, operator, b)

    if user_answer == correct_answer:
        print_correct_answer()
        return True
    else:
        print_wrong_answer(user_answer, correct_answer)
        return False


def brain_calc(name: str):
    print('What is the result of the expression?')
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
    brain_calc(name)


if __name__ == "__main__":
    main()
