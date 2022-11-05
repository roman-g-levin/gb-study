﻿"""
Создайте программу для игры с конфетами человек
против человека.
Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать
все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""
import random

print('Программа игры двух человек в 2021 конфету')
konf = 2021   # осталось конфет
pkonf = {1: 0, 2: 0}

# жеребъевка игроков
random.seed
player = random.randint(1, 2)
print(f'Первым ходит игрок {player}')

while konf > 0:
    print(f'На столе {konf} конфет, у игроков: {pkonf}')
    if konf < 28:
        max_pget = konf
    else:
        max_pget = 28
    print(f'Игрок {player} может взять от 1 до {max_pget}')
    pget = int(input(f'Введите число конфет, которое взял игрок {player}:'))
    if pget > max_pget or pget < 1:
        print('Неверный ввод')
        continue
    pkonf[player] += pget
    konf -= pget
    if player == 1:
        player = 2
    else:
        player = 1

print('Конфеты кончились')
if player == 1:
    player = 2
else:
    player = 1
print(f'Последнюю взял игрок {player}')
