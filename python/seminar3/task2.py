"""Задача 2
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

import random

print('Программа вывода произведений пар чисел')
random.seed
N = random.randint(1, 8)

list = []
for i in range(N):
    list.append(random.randint(0, 10))

prod = []
if len(list) % 2 == 0:
    for i in range(N//2):
        prod.append(list[i]*list[len(list)-1-i])
else:
    for i in range(N//2+1):
        prod.append(list[i]*list[len(list)-1-i])

print(f'{list} -> {prod}')
