import scipy.stats as stats
import numpy as np

print("Теория вероятностей и математическая статистика")
print("Семинар 7. Непараметрические тесты")
print("Задача 2:\n\
Исследовалось влияние препарата на уровень давления пациентов. Сначала \
измерялось давление до приема препарата, потом через 10 минут и через 30 минут. \
Есть ли статистически значимые различия между измерениями давления?\n\
В выборках не соблюдается условие нормальности.\n\
1е измерение до приема препарата: 150, 160, 165, 145, 155\n\
2е измерение через 10 минут: 140, 155, 150, 130, 135\n\
3е измерение через 30 минут: 130, 130, 120, 130, 125\n")

α=0.05
data1 = np.array([150, 160, 165, 145, 155])
data2 = np.array([140, 155, 150, 130, 135])
data3 = np.array([130, 130, 120, 130, 125])

print(f"Решение 2:\n\
Анализ повторных измерений, 3 группы данных.\n\
Выбран критерий Фридмана, α={α}.\n\
H0: статистически значимых различий нет\n\
H1: имеются статистически значимые различия\n")

print(stats.friedmanchisquare(data1, data2, data3))

statistic, pvalue = stats.friedmanchisquare(data1, data2, data3)
msg = 'H0 принимается, статистически значимых отличий нет' if α < pvalue \
    else 'H0 отвергается, принимается H1, есть статистически значимые отличия'
print(f'{msg}')
