"""Эадача 1
Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

"""
рефакторинг кода - подсчет результата с использованием функций filter, map, lambda
"""

import random

print('Программа нахождения суммы элементов списка на нечетных позициях')
random.seed
N = random.randint(1, 10)


def even(x):
    return x % 2


lis = []
evenodd = []
for i in range(N):
    lis.append(random.randint(0, 10))
    evenodd.append(even(i))
print(f'Сгенерирован список     {lis}')
print(f'Четные и нечетные места {evenodd}')

res = sum(filter(lambda x:(x != 0), map(lambda x,y:x*y, lis, evenodd)))
print(f'Сумма элементов на нечетных позициях:{res}')
