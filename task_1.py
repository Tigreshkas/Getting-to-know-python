# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_mulpiplier(k):
    """Функция проверки числа на натуральность,
    также выводит список простых множителей введенного числа"""
    multiplier = []
    plier = [2, 3, 5, 7]
    if k == 1:
        multiplier.append(int(k))
    elif k < 1 or type(k) is float:
        return f'Введено ненатуральное число!'
    else:
        while k != 1:
            if k % 2 != 0 and k % 3 != 0 and k % 5 != 0 and k % 7 != 0:
                multiplier.append(int(k))
                k = 1
            else:
                for i in plier:
                    if k % i == 0:
                        multiplier.append(i)
                        k /= i
                        break
    return multiplier


if __name__ == '__main__':
    num = int(input('Введите натуральное число: '))
    print(f'Простые множители числа {num}: {simple_mulpiplier(num)}')
