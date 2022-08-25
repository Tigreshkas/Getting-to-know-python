# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    """Функция нахождения чисел Фибоначчи."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def negafibonacci(k):
    """Функция нахождения чисел Негафибаначчи."""
    if k == -1:
        return 1
    elif k == -2:
        return -1
    elif k != 0:
        return negafibonacci(k + 2) - negafibonacci(k + 1)


num = 8  # для k = 8
# num = int(input('Введите k: '))  # для любого k (если нужно любое число)
num_fib = []
for i in range(- num, 0):
    num_fib.append(negafibonacci(i))
for i in range(num + 1):
    num_fib.append(fibonacci(i))
print(f'Для k = {num} -> {num_fib}')
