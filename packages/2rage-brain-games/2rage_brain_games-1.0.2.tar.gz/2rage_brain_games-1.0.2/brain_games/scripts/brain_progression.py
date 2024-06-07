import random
from brain_games.game_logic import (
    print_user_lose,
    print_user_win,
    get_user_answer_integer,
    print_question,
    print_correct_answer,
    print_wrong_answer,
)
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.constants import MAX_ATTEMPTS


def generate_progression(first_num, difference, n):
    progression = []
    current_item = first_num
    for _ in range(n):
        progression.append(current_item)
        current_item += difference
    return progression


def progression_remove_random_index(progression):
    if not progression:
        print('Error, progression is empty')
        return None

    index_to_remove = random.randint(0, len(progression) - 1)
    removed_number = progression.pop(index_to_remove)
    progression.insert(index_to_remove, '..')
    return removed_number


def format_progression(progression):
    return ' '.join(map(str, progression))


def handle_game_round(name):
    rnd_num = random.randint(1, 10)
    rnd_diff = random.randint(1, 10)
    rnd_n = random.randint(5, 15)
    random_progresison = generate_progression(rnd_num, rnd_diff, rnd_n)
    removed_number = progression_remove_random_index(random_progresison)

    question = format_progression(random_progresison)
    print_question(question)

    user_answer = get_user_answer_integer()

    if removed_number == user_answer:
        print_correct_answer()
        return True
    else:
        print_wrong_answer(user_answer, removed_number)
        return False


def brain_progression(name):
    print('What number is missing in the progression?')

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
    brain_progression(name)


if __name__ == '__main__':
    main()
