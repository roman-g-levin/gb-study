# ------------------------------------------- 2 -----------------------------
# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и
# произведение * дробей. Для проверки своего кода используйте модуль fractions.

def calculate_fraction_operations(fraction1, fraction2):
    num_1, denom_1 = map(int, fraction1.split('/')) # 1/3 -> ["1", "3"] -> [1, 3]
    num_2, denom_2 = map(int, fraction2.split('/'))

    # Вычисляем сумму и произведение числителей
    num_add = num_1 * denom_2 + num_2 * denom_1
    num_mult = num_1 * num_2

    # Вычисляем знаменатель для обеих операций
    denom_common = denom_1 * denom_2

    # Сокращаем полученные дроби
    gcd_add = greatest_common_divisor(num_add, denom_common)
    gcd_mult = greatest_common_divisor(num_mult, denom_common)

    addition = f"{num_add // gcd_add}/{denom_common // gcd_add}"
    multiplication = f"{num_mult // gcd_mult}/{denom_common // gcd_mult}"

    return addition, multiplication


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


f_1 = input("Введите первую дробь в формате a/b: ")
f_2 = input("Введите вторую дробь в формате a/b: ")

add, mult = calculate_fraction_operations(f_1, f_2)

print("Сумма дробей:", add)
print("Произведение дробей:", mult)

# Проверка с использованием модуля fractions
from fractions import Fraction

f1 = Fraction(f_1)
f2 = Fraction(f_2)

print("Проверка с использованием модуля fractions:")
print("Сумма дробей (fractions):", f1 + f2)
print("Произведение дробей (fractions):", f1 * f2)
