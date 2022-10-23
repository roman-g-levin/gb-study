"""
Задайте последовательность чисел.
Напишите программу, которая выведет
список неповторяющихся элементов исходной
последовательности.
"""

import random

print('Программа вывода списка неповторяющихся элементов')
random.seed
N = random.randint(5, 30)

list = []
for i in range(N):
    list.append(random.randint(1, 20))
print(f'Сгенерирован список: {list}')

res = []
for i in list:
    if i in res:
        continue
    else:
        res.append(i)
print(f'Список неповторяющихся элементов: {res}')
