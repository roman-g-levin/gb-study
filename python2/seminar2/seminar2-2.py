'''

2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
    строковое представление. Функцию hex используйте для проверки своего результата.

'''

HEX: int = 16
HEXDIGITS = '0123456789ABCDEF'

num: int = int(input('Введите число: '))

print(f'Стандартная функция: {hex(num)}')

if num == 0:
    result = '0'
else:
    result: str = ''
    while num > 0:
        result = HEXDIGITS[num % HEX] + result
        num //= HEX

print(f'Результат: {result}')
