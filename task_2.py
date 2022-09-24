# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def checking_1(user, check):
    if user == 'Игрок':
        try:
            cand_1 = int(input(f'{user} берет от 1 до {"28" if check > 28 else check} конфет: '))
        except ValueError:
            print('Введите число!')
            return checking_1(user, check)
        else:
            if cand_1 < 1 or cand_1 > 28:
                print('Нельзя брать меньше 1 или больше 28 конфет!')
                return checking_1(user, check)
            else:
                if cand_1 > check:
                    print(f'Можно взять не более {check} конфет.')
                    return checking_1(user, check)
                else:
                    return cand_1
    else:
        cand_2 = random.randint(1, 28)
        if cand_2 > check:
            cand_2 = random.randint(1, check)
            print(f'Компьютер берет {cand_2} конфет.')
            return cand_2
        else:
            print(f'Компьютер берет {cand_2} конфет.')
            return cand_2


def game(users_play, candy_all):
    """Логика игры"""
    full_candies = 2021
    count = 0
    while full_candies > 0:
        if count == 0:
            candy_1 = checking_1(users_play[0], full_candies)
            count = 1
            full_candies -= candy_1
            candy_all[0] += candy_1
        else:
            candy_2 = checking_1(users_play[1], full_candies)
            count = 0
            full_candies -= candy_2
            candy_all[1] += candy_2
    print(f'У {users_play[0]}а {candy_all[0]} конфет.\n'
          f'У {users_play[1]}а {candy_all[1]} конфет.')
    return f'Игра закончена. {users_play[0] if count == 1 else users_play[1]} забрал последние конфеты и выигал!'


num = random.randint(1, 2)
users = []
print('Игра началась!')
if num == 1:
    print('Первым ходит Игрок.')
    users.append('Игрок')
    users.append('Компьютер')
else:
    print('Первым ходит Компьютер.')
    users.append('Компьютер')
    users.append('Игрок')
print(game(users, [0, 0]))
