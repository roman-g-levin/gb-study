"""
Задача 1
Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
    Пример:
- 6782 -> 23
- 0,56 -> 11
"""

print('Программа подсчета суммы цифр в числе')
num = float(input('Введите вещественное число: '))

num_str = str(num)
summ = 0
for c in num_str:
    if c.isdigit():
        summ += int(c)
print(f'{num} -> {summ}')