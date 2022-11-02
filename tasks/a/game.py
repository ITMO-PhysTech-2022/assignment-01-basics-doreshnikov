"""
Игра "Быки и коровы"

Компьютер загадывает строку из n цифр.
Каждый ход игрок вводит догадку - тоже строку из n цифр, и получает в ответ
- количество "быков" - верно угаданных цифр на своих позициях
- количество "коров" - верно угаданных цифр, поставленных на неверные позиции

Например, при загаданной строке "4271" и догадке "1234" есть
- 1 бык - цифра "2" на второй позиции
- 2 коровы - цифры "1" и "4"

Реализуйте вспомогательные функции для этой игры:
- [a] create_secret, score, validate
- [b] computer
- [*] сделайте так, чтобы игрок-компьютер опирался на результаты
  предыдущих ходов и пытался делать основанные на них ходы
    > вам придется заметно изменить структуру игры, чтобы
      иметь возможность сообщать игроку результаты по-разному
      в зависимости от того, человек это или компьютер
"""

from typing import Callable
from random import choices, randint


def create_secret(n: int) -> str:
    """
    Функция принимает длину загадываемого числа
    и возвращает случайную строку из цифр указанной длины
    """

    # решение с использованием random.choices - выбор случайного элемента
    d = [str(i) for i in range(10)]  # ['0', '1', ..., '9']
    s = ''.join(choices(d, k=n))  # выбрать n случайных цифр и склеить в одну строку

    # более простое решение - n раз добавляем к пустой строке случайную цифру
    s = ''
    for i in range(n):
        s += str(randint(0, 9))
    return s


def score(secret: str, guess: str) -> tuple[int, int]:
    """
    Функция принимает загаданную строку и догадку игрока
    и возвращает пару из количества "быков" и количества "коров"
        > можно для каждой цифры от '0' до '9' посмотреть на позиции
          ее вхождения в secret и guess
        > для нахождения числа общих позиций может быть полезно
          воспользоваться структурой данных "множество" (set)
    """

    # базовое решение для подсчета быков
    bulls = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1

    # более компактное решение для подсчета быков
    bulls = 0
    for c1, c2 in zip(secret, guess):
        bulls += c1 == c2

    # неадекватное решение для подсчета быков
    bulls = len(set(enumerate(secret)) & set(enumerate(guess)))

    # дальше считаем быков и коров вместе
    # каждая цифра является быком или коровой min(count1, count2) раз
    # где count1 и count2 - количество ее вхождений в secret и guess
    cows_plus_bulls = 0
    for c in range(10):
        cows_plus_bulls += min(secret.count(str(c)), guess.count(str(c)))

    # то же самое, но записанное через list comprehension
    cows_plus_bulls = sum([min(secret.count(str(c)), guess.count(str(c)))
                           for c in range(10)])

    # коровы = (коровы + быки) - быки
    return bulls, cows_plus_bulls - bulls


def validate(n: int, guess: str) -> bool:
    """
    Функция принимает параметр игры - длину загаданной строки, и догадку игрока
    и возвращает, правда ли игрок ввел корректную догадку (строку длины n из цифр)
    """

    # проверка длины
    if len(guess) != n: return False

    # проверка, что каждый символ - цифра
    digits = [str(i) for i in range(10)]
    for c in guess:
        if c not in digits:
            # если хотя бы один символ - не цифра, сразу возвращаем False
            return False
    return True

    # альтернативный способ проверить, что каждый символ - цифра
    return guess.isnumeric()


def computer_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, генерирующую догадки
    """

    # будем по очереди называть все догадки от 000..00 до 999..99
    last_guess = -1
    # форматная строка, используемая для дополнения числа нулями до длины n
    formatter = f'{{:0>{n}}}'

    def guess():
        nonlocal last_guess
        last_guess += 1
        result = formatter.format(last_guess)
        print(f'My guess is \'{result}\'')
        return result

    return guess


def real_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, получающую догадку от реального игрока
    """
    print(f'The secret word has length {n}')
    return input


def play(n: int, player: Callable):
    """
    Функция реализует процесс игры с заданной длиной слова и игроком
    """
    secret = create_secret(n)
    attempts = 0
    while True:
        guess = player()
        attempts += 1
        if not validate(n, guess):
            print(f'Your guess should be a string of {n} digits')
            continue
        bulls, cows = score(secret, guess)
        if bulls == n:
            print(f'Correct! You\'ve won in {attempts} guesses')
            break
        else:
            print(f'Your guess has {bulls=} and {cows=}')


if __name__ == '__main__':
    n = 4
    play(n, computer_player(n))
