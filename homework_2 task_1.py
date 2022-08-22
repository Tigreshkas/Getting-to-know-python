# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num_str = input('Введите любое число: ')
num = int(''.join(i for i in num_str if i.isdecimal()))
sum_num = 0

while num != 0:
    num_last = num % 10
    sum_num += num_last
    num = num // 10

print(f'Сумма цифр числа {num_str} = {int(sum_num)}')
