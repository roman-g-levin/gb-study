"""
5. Напишите программу, которая принимает на вход координаты
двух точек и находит расстояние между ними в 2D пространстве.
Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

from math import sqrt


print('Программа нахождения расстояния между двумя точками в 2D пространстве')
x1 = int(input('Введите координату X1 ->'))
y1 = int(input('Введите координату Y1 ->'))
x2 = int(input('Введите координату X2 ->'))
y2 = int(input('Введите координату Y2 ->'))

print(f'A ({x1},{y1}); B ({x2},{y2}) -> {round(sqrt(((x2-x1)**2)+((y2-y1)**2)),4)}')
