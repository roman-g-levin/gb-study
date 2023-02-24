from math import factorial

def C(k,n):
    '''
    Функция расчета количества сочетаний из n по k
    '''
    return factorial(n)/(factorial(k)*factorial(n-k))


print("Теория вероятностей и математическая статистика")
print("Семинар 3. EDA (exploratory data analysis) или Разведочный анализ")
print("Задание 2:\n\
В первом ящике находится 8 мячей, из которых 5 - белые.\n\
Во втором ящике - 12 мячей, из которых 5 белых.\n\
Из первого ящика вытаскивают случайным образом два мяча,\n\
из второго - 4. Какова вероятность того, что 3 мяча белые?")

print("Решение 2:")

# количество мячей в ящиках
n1=8
n1b=5
n1nb=n1-n1b

n2=12
n2b=5
n2nb=n2-n2b

## считаем вероятность вытащить 3 белых мяча при:
# 2 мяча из первого ящика и 4 из второго
## первый случай:
# 2 белых из 5 из первого ящика
c1b=C(2,n1b)
# 0 небелых 
c1nb=C(0,n1nb)
# вероятность вынуть 2 белых мяча из первого ящика
p1b2=c1b*c1nb/C(2,n1)
# вероятность вынуть 1 белых и 3 небелых мяча из второго ящика
p2b1=C(1,n2b)*C(3,n2nb)/C(4,n2)
# итоговая вероятность вынуть 2 белых из 1 ящика и 1 белый из второго
p1=p1b2*p2b1

## второй случай
# вероятность вынуть 1 белый мяч и 1 небелый из первого ящика
p1b1=C(1,n1b)*C(1,n1nb)/C(2,n1)
# вероятность вынуть 2 белых мяча и 2 небелый из второго ящика
p2b2=C(2,n2b)*C(2,n2nb)/C(4,n2)
# итоговая вероятность вынуть 1 белый из 1 ящика и 2 белых из второго
p2=p1b1*p2b2

## третий случай
# вероятность вынуть 0 белых мячей и 2 небелых из первого ящика
p1b0=C(0,n1b)*C(2,n1nb)/C(2,n1)
# вероятность вынуть 3 белых мячей и 1 небелых из второго ящика
p2b3=C(3,n2b)*C(1,n2nb)/C(4,n2)
# итоговая вероятность вынуть 2 белых из 1 ящика и 0 небелых из второго
p3=p1b0*p2b3

## Итоговая вероятность вынуть ровно 3 белых мяча из двух ящиков - это
# сумма трех вероятностей
p=p1+p2+p3
print (f"Вероятность вынуть ровно 3 белых мяча из обоих ящиков составляет: {p}\n\
-------\n")
