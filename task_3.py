# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def random_sign(math_expr):
    """Функция для случайной генерации знака выражения."""
    sign = random.randint(1, 2)
    if sign == 1:
        return f'+ {math_expr}'
    else:
        return f'- {math_expr}'


def expression(expr):
    """Функция для корректного написания выражения в зависимости от степени."""
    if expr == 1:
        return f'x'
    else:
        return f'x^{expr}'


def random_exp(deg):
    """Функция для написания выражения многочлена со случайными числами (от 0 до 100)."""
    num = random.randint(0, 100)
    if num == 0:
        return '1'
    elif num == 1:
        return f'{expression(deg)}'
    else:
        return f'{num}*{expression(deg)}'


def random_polynomial(degree):
    """Функция для написания многочлена с рандомными коэффициентами."""
    polynominal = []
    poly_1 = random_sign(random_exp(degree))
    if list(poly_1)[0] == '+':  # для красоты вывода (если первое выражение в многочлене положит., то "+" не выводится)
        polynominal.append(poly_1[2:])
    else:
        polynominal.append(poly_1)
    degree -= 1
    while degree != 0:
        a = random.randint(1, 2)
        if a == 1:  # рандомно выбирается будет ли отдельное выражение с определенной степенью в многочлене или нет
            polynominal.append(random_sign(random_exp(degree)))
            degree -= 1
        else:
            degree -= 1
    polynominal.append('= 0')
    poly_str = " ".join(polynominal)
    return poly_str


k = int(input('Введите натуральную степень: '))
n = int(input('Сколько многочленов требуется создать: '))
if k < 1:
    print('Введена ненатуральная степень!')
else:
    with open('polynominal.txt', 'w', encoding='utf-8') as file_poly:  # запись многочленов в файл
        # (для каждой степени файл перезаписывается)
        while n != 0:
            print(f'k = {k} -> {random_polynomial(k)}', file=file_poly)
            n -= 1
    with open('polynominal.txt', 'r', encoding='utf-8') as file_1:  # вывод данных на терминал из файла построчно
        while True:
            row = file_1.readline()
            print(row, end='')
            if not row:
                break
