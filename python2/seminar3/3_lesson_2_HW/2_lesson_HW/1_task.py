# ------------------------------------------- 1 -----------------------------
# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def get_hexadecimal_representation(number):
    hexadecimal = ""

    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    while number > 0:
        remainder = str(number % 16)
        hexadecimal = remainder + hexadecimal
        number = number // 16

    if is_negative:
        hexadecimal = "-" + hexadecimal

    return hexadecimal


num = int(input("Введите целое число: "))
result = get_hexadecimal_representation(num)
print("Шестнадцатеричное представление числа:", result)
print("Шестнадцатеричное представление числа через hex: ", hex(num))

