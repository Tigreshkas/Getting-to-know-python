# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def non_repeat(sequence):
    """Функция для выявления неповторяющихся элементов последовательности."""
    new_seq = []
    for i in sequence:
        if i not in new_seq:
            new_seq.append(i)
    return new_seq


# seq = [4, 2, 6, 8, 2, 6, 9, 5]  # для быстрой проверки
# print(f'{seq} -> {non_repeat(seq)}')
seq = input('Введите список элементов через пробел: ')
seq_list = list(map(int, seq.split()))
print(f'{seq_list} -> {non_repeat(seq_list)}')
