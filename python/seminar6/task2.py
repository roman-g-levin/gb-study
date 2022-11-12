"""Задача 2
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

"""
рефакторинг - обработка списка первый-последний сделана через рекурсию
"""

import random
prod = []

def umn(mass):
    if len(mass)==0:
        return
    elif len(mass)==1:
        prod.append(mass[0]**2)
        return
    else:
        prod.append(mass[0]*mass[-1])
        umn(mass[1:-1])

print('Программа вывода произведений пар чисел')
random.seed
N = random.randint(1, 8)

list = []
for i in range(N):
    list.append(random.randint(0, 10))

umn(list)
print(f'{list} -> {prod}')
