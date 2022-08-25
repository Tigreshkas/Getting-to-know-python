# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def multi_pairs(num_list):
    list_copy = num_list.copy()  # создаю копию списка, чтобы можно было удалять использованные элементы
    new_list = []
    while list_copy:  # пока список не пустой выполняем цикл
        if len(list_copy) > 1:
            new_list.append(list_copy[0] * list_copy[-1])
            list_copy.remove(list_copy[0])
            list_copy.remove(list_copy[-1])
        else:
            new_list.append(list_copy[0] ** 2)
            list_copy.remove(list_copy[0])
    return new_list


list_1 = [2, 3, 4, 5, 6]
print(f'Произведение пар чисел списка: \n{list_1} => {multi_pairs(list_1)}')
list_2 = [2, 3, 5, 6]
print(f'{list_2} => {multi_pairs(list_2)}')
