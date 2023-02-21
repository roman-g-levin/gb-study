from math import factorial

def C(k,n):
    '''
    Функция расчета количества сочетаний из n по k
    '''
    return factorial(n)/(factorial(k)*factorial(n-k))


print("Теория вероятностей и математическая статистика")
print("Семинар 2. Дискретные распределения вероятностей")
print("Задание 4:\n\
В первом ящике находится 10 мячей, из которых 7 - белые.\n\
Во втором ящике - 11 мячей, из которых 9 белых.\n\
Из каждого ящика вытаскивают случайным образом по два мяча.\n\
а) Какова вероятность того, что все мячи белые?\n\
б) Какова вероятность того, что ровно два мяча белые?\n\
в) Какова вероятность того, что хотя бы один мяч белый?\
")

print("Решение 4а:")

# количество мячей по ящикам
n1=10
n1b=7
n1nb=n1-n1b

n2=11
n2b=9
n2nb=n2-n2b

# количество извлекаемых мячей
# всего, белых и небелых из ящиков 1 и 2
k1=2
k1b=2
k1nb=0

k2=2
k2b=2
k2nb=0

# считаем сочетание вариантов для первого ящика
# 2 белых из 7
c1b=C(k1b,n1b)
# 0 небелых из (10-7)
c1nb=C(k1nb,n1nb)
# вероятность вынуть 2 белых мяча из первого ящика
p1=c1b*c1nb/C(k1,n1)

# считаем сочетание вариантов для второго ящика
# 2 белых из 9
c2b=C(k2b,n2b)
# 0 небелых из (11-9)
c2nb=C(k2nb,n2nb)
# вероятность вынуть 2 белых мяча из первого ящика
p2=c2b*c2nb/C(k2,n2)

# события по выниманию мячей из первого и второго ящиков независимы,
# поэтому итоговая вероятность вынуть по 2 белых мяча из обоих ящиков
# есть произведение вероятностей для каждого ящика
p=p1*p2
print (f"Вероятность вынуть по 2 белых мяча из обоих ящиков составляет: {p}\n\
-------\n")

print("Решение 4б:")
## первый случай
# 2 белых из 7 из первого ящика
c1b=C(2,n1b)
# 0 небелых из (10-7)
c1nb=C(0,n1nb)
# вероятность вынуть 2 белых мяча из первого ящика
p1b2=c1b*c1nb/C(k1,n1)
# вероятность вынуть 0 белых и 2 небелых мяча из второго ящика
p2nb2=C(0,n2b)*C(2,n2nb)/C(k2,n2)
# итоговая вероятность вынуть 2 белых из 1 ящика и 0 небелых из второго
p1=p1b2*p2nb2

## второй случай
# вероятность вынуть 1 белый мяч и 1 небелый из первого ящика
p1b1=C(1,n1b)*C(1,n1nb)/C(k1,n1)
# вероятность вынуть 1 белый мяч и 1 небелый из второго ящика
p2b1=C(1,n2b)*C(1,n2nb)/C(k2,n2)
# итоговая вероятность вынуть 1 белый из 1 ящика и 1 белый из второго
p2=p1b1*p2b1

## третий случай
# вероятность вынуть 0 белых мячей и 2 небелых из первого ящика
p1b0=C(0,n1b)*C(2,n1nb)/C(k1,n1)
# вероятность вынуть 2 белых мячей и 0 небелых из второго ящика
p2b2=C(2,n2b)*C(0,n2nb)/C(k2,n2)
# итоговая вероятность вынуть 2 белых из 1 ящика и 0 небелых из второго
p3=p1b0*p2b2

## Итоговая вероятность вынуть ровно 2 белых мяча из двух ящиков - это
# сумма трех вероятностей
p=p1+p2+p3
print (f"Вероятность вынуть ровно 2 белых мяча из обоих ящиков составляет: {p}\n\
-------\n")

print("Решение 4в:")
# вероятность появления хотя бы одного белого мяча в выборке составляет
# полную группу событий с вероятностью появления в выборке
# всех небелых мячей

# вероятность вынуть 0 белых мячей и 2 небелых из первого ящика
p1nb2=C(0,n1b)*C(2,n1nb)/C(k1,n1)
# вероятность вынуть 0 белых и 2 небелых мяча из второго ящика
p2nb2=C(0,n2b)*C(2,n2nb)/C(k2,n2)
# итоговая вероятность вынуть 4 небелых мяча из обоих ящиков
p=p1nb2*p2nb2
# вероятность того, что хотя бы один мяч будет белый
q=1-p

print (f"Вероятность того, что хотя бы один мяч будет белый составляет: {q}")