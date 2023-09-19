'''
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
    и знаменателем. Программа должна возвращать сумму и произведение* дробей.
    Для проверки своего кода используйте модуль fractions.
'''
import math
import fractions

print('Программа работы с дробями')
print('Введите две дроби вида a/b и c/d')

while True:
    first = input('Введите первую дробь a/b: ')
    first_splitted = first.split(sep='/')
    if len(first_splitted) != 2:
        print('Ошибка ввода')
        continue
    if first_splitted[0].isnumeric() and first_splitted[1].isnumeric:
        a = int(first_splitted[0])
        b = int(first_splitted[1])
        break
    else:
        print('Ошибка ввода')
        continue

while True:
    second = input('Введите вторую дробь c/d: ')
    second_splitted = second.split(sep='/')
    if len(second_splitted) != 2:
        print('Ошибка ввода')
        continue
    if second_splitted[0].isnumeric() and second_splitted[1].isnumeric:
        c = int(second_splitted[0])
        d = int(second_splitted[1])
        break
    else:
        print('Ошибка ввода')
        continue

print(f'Первая дробь: {a}/{b}')
print(f'Вторая дробь: {c}/{d}')

# сложение дробей
add_top = a * d + c * b
add_bottom = b * d
add_gcd = math.gcd(add_top,add_bottom)
top, bottom = int(add_top/add_gcd), int(add_bottom/add_gcd)
if bottom ==1:
    print(f'Результат сложения: {top}')
else:
    print(f'Результат сложения: {top}/{bottom}')

# умножение дробей
mul_top = a * c
mul_bottom = b * d
mul_gcd = math.gcd(mul_top,mul_bottom)
top, bottom = int(mul_top/mul_gcd), int(mul_bottom/mul_gcd)
if bottom ==1:
    print(f'Результат умножения: {top}')
else:
    print(f'Результат умножения: {top}/{bottom}')

# проверка
f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)
print(f'Проверка сложение: {f1} + {f2} = {f1 + f2}')
print(f'Проверка произведениe: {f1} * {f2} = {f1 * f2}')
