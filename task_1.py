# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = 'jdjdw kabckawe x jkwjhhqd abc jwjenm'
txt_list = txt.split()
new = [i for i in txt_list if 'abc' not in i]
new_str = ' '.join(new)
print(f'Исходный текст: {txt}')
print(f'Исправленный текст: {new_str}')
