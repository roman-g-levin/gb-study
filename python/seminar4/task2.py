"""
Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.
"""

# список с простыми числами
simples = []

# функция нахождения всех простых чисел от 1 до n
def find_simples(n):
    for i in range(2, n+1):
        simple = True
        for j in range(2, i):
            if i//j*j == i:
                simple = False
                continue
        if simple:
            simples.append(i)

# функция поиска простых делителей числа
def find_prod(n):
    res=[]
    num = n
    while num>1:
        for i in simples:
            if int(num/i)*i==num:
                res.append(i)
                num=num/i
                break
    return res

print('Программа нахождения простых множителей числа N')
N = int(input('Введите натуральное число N:'))
if N <= 0:
    print('Некорректный ввод')
else:
    find_simples(N)  # найти простые числа
    print(f'Найдены простые числа для поиска делителей:\n{simples}')
    print(f'Простные делители числа {N} -> {find_prod(N)}')
