import prompt
from colorama import Fore


def get_user_answer_integer():
    """Получение ответа от пользователя."""
    try:
        user_answer = int(prompt.string('Your answer: '))
        return user_answer
    except ValueError:
        print('Please enter a valid integer.')


def get_user_answer_string():
    return prompt.string('Your Answer ')


def print_question(question, extra_info1="", extra_info2=""):
    """Вывод вопроса на экран."""
    if extra_info1 and extra_info2:
        print(f'Question: {question} {extra_info1} {extra_info2}')
    elif extra_info1:
        print(f'Question: {question} {extra_info1}')
    else:
        print(f'Question: {question}')


def print_user_win(name):
    print(f'Congratulations, {Fore.CYAN}{name}{Fore.RESET}!')


def print_user_lose(name):
    print(f"Let's try again, {Fore.CYAN}{name}{Fore.RESET}!")


def print_correct_answer():
    """Вывод сообщения о правильном ответе."""
    print(f'{Fore.GREEN}Correct!{Fore.RESET}')


def print_wrong_answer(usr_ans, ok_ans):
    """Вывод сообщения о неправильном ответе."""
    print(f'{usr_ans}is wrong answer ;(. Correct answer was {ok_ans}')
