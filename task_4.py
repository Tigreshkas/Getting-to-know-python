# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_number(num):
    """Функция перевода десятеричного числа в двоичное."""
    num_list = []
    while num >= 1:
        if int(num) % 2 == 0:
            num_list.append(0)
        else:
            num_list.append(1)
        num /= 2
    res = ''.join(map(str, reversed(num_list)))
    return res


num_1 = int(input('Введите число: '))
print(f'{num_1} -> {binary_number(num_1)}')
