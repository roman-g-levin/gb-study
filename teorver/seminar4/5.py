import math

print("Теория вероятностей и математическая статистика")
print("Семинар 4. Непрерывная случайная величина")
print("Задание 5:\n\
На сколько сигм (средних квадратичных отклонений) отклоняется рост\n\
человека, равный 190 см, от математического ожидания роста в популяции,\n\
в которой M(X) = 178 см и D(X) = 25 кв.см?")

# из условий
x=190
M=178
D=25
σ=math.sqrt(D)

# расчет отклонения
z=(x-M)/σ

print(f"Решение 5:\n\
Отклонение роста в сигмах составляет: {z}")
