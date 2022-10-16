"""
Задача 4
Задайте список из N элементов, заполненных числами из
промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
Реализуйте алгоритм перемешивания списка.
"""

import random
import sys

"""Задайте список из N элементов, заполненных числами из
промежутка [-N, N]."""
print('Программа работы со списком из N элементов')
N = int(input('Введите целое положительное число N: '))
if N <= 0:
    print('Некорректный ввод')
else:
    list=[]
    random.seed
    for i in range(N):
        list.append(random.randint(-N, N))
    print(f'Сгенерирован список {list}')

    """Найдите произведение элементов на указанных позициях.
    Позиции хранятся в файле file.txt в одной строке одно число."""
    file_to_read = open("file.txt", "r")
    readed_lines = file_to_read.readlines()
    file_to_read.close
    print(f'Считаны строки из файла file.txt {readed_lines}')
    readed_index=[]
    for i in range(len(readed_lines)):
        readed_index.append(int(readed_lines[i]))
    print(f'Считаные строки преобразованы в целые числа {readed_index}')
    prod=1
    for n in readed_index:
        if n>=len(list):
            print(f'Индекс {n} из файла за пределами списка')
        else:
            prod*=list[n]
    print(f'Произведение чисел на позициях из списка {prod}')
        
    """Реализуйте алгоритм перемешивания списка."""
    random.shuffle(list)
    print(f'Перемешанный список {list}')    
