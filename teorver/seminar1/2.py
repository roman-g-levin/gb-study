from math import factorial

print("Теория вероятностей и математическая статистика")
print("Семинар 1. Расчет вероятности случайных событий")
print("Задание 2:\n\
На входной двери подъезда установлен кодовый замок,\n\
содержащий десять кнопок с цифрами от 0 до 9.\n\
Код содержит три цифры, которые нужно нажать одновременно.\n\
Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?\
")

print("Решение 2:")

# количество кнопок
n=10

# количество кнопок, подлежащих одновременному нажатию
k=3

# количество правильных вариантов нажатия
m=1

# считаем сочетание вариантов 3 из 10
# т.к. кнопки нажимаются одновременно,
# порядок нажатия не важен и нас интересует расчет сочетания
c=factorial(n)/(factorial(k)*factorial(n-k))

# расчет вероятности
p=m/c

print(f"Вероятность угадать 3 цифры из 10 составляет: {p}")
