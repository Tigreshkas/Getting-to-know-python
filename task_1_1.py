# Показать разбиение на простые множители всех чисел от 0 до N (30000).

from task_1 import simple_mulpiplier

n = 30000
# n = int(input('Введите N: '))  # на случай, если N должно быть любым числом
for i in range(1, n + 1):
    print(f'Простые множители числа {i}: {simple_mulpiplier(i)}')
