# Реализуйте алгоритм перемешивания списка.

import random

num_list = [0, 1, 2, 3, 4, 5]
print(f'Изначальный список: {num_list}')
print(f'Пересортированный список: {random.sample(num_list, len(num_list))}')
