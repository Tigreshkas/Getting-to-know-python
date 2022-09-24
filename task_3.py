# Создайте программу для игры в ""Крестики-нолики"".

# В данном случае реализована игра между двумя реальными игроками
import random


def make_field(num):
    """Функция для отрисовки сетки"""
    print('|', num[0], '|', num[1], '|', num[2], '|')
    print('---- --- ----')
    print('|', num[3], '|', num[4], '|', num[5], '|')
    print('---- --- ----')
    print('|', num[6], '|', num[7], '|', num[8], '|')


def choose_square(square, elem):
    """Функция для назначения позиции"""
    while True:
        if field[square - 1] != ' ':
            square = int(input('Данная позиция занята. Поставьте на другую: '))
        else:
            field[square - 1] = elem
            make_field(field)
            break


def win_game(elem):
    """Функция определения победы"""
    if field[0] == field[1] == field[2] == elem or field[3] == field[4] == field[5] == elem or \
            field[6] == field[7] == field[8] == elem or field[0] == field[3] == field[6] == elem or \
            field[1] == field[4] == field[7] == elem or field[2] == field[5] == field[8] == elem or \
            field[0] == field[4] == field[8] == elem or field[2] == field[4] == field[6] == elem:
        return 1


def game(gamer_1, gamer_2):
    """Логика игры"""
    draw = 0
    while True:
        res_1 = int(input(f'{gamer_1} ставит Х на позицию (цифра от 1 до 9): '))
        choose_square(res_1, 'x')
        draw += 1
        if win_game('x') == 1:
            print(f'Победа! Выграл игрок {gamer_1}.')
            break
        if draw == 9:
            print('Ничья!')
            break
        res_2 = int(input(f'{gamer_2} ставит O на позицию (цифра от 1 до 9): '))
        choose_square(res_2, 'o')
        draw += 1
        if win_game('o') == 1:
            print(f'Победа! Выграл игрок {gamer_2}.')
            break
        if draw == 9:
            print('Ничья!')
            break


field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
field_2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print('Номера позиций:')
make_field(field_2)
user_1 = 'Игрок 1'
user_2 = 'Игрок 2'
queue = random.randint(1, 2)
if queue == 1:  # рандомно выбирается у кого будет первый ход
    print(f'Первым ходит {user_1}.')
    game(user_1, user_2)
else:
    print(f'Первым ходит {user_2}.')
    game(user_2, user_1)
