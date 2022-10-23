"""
Задана натуральная степень k. Сформировать
случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать
в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random

print('Программа записи в файл случайно сгенерированного многочлена степени k')
random.seed
k = int(input('Введите степень k:'))
if k<0:
    print('Некорректный ввод')
else:

    list = []
    for i in range(k+1):
        list.append(random.randint(1, 101))
    print(f'Сгенерирован список коэффициентов: {list}')
    for i in range(k,0,-1):
        print(f'{list[i]}*x**{i} + ',end='')
    print(f'{list[0]}')

    with open('task4.txt','w') as data:
        for i in range(k,0,-1):
            data.write(f'{list[i]}*x**{i} + ')
        data.write(f'{list[0]}\n')
