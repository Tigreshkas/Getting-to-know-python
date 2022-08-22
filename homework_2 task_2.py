# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def recurs(n):
    if n == 0:
        return 1
    return n * recurs(n - 1)


num = int(input('Введите число: '))
print(f'Произведение чисел от 1 до {num} = {recurs(num)}')
