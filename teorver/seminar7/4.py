import scipy.stats as stats
import numpy as np

print("Теория вероятностей и математическая статистика")
print("Семинар 7. Непараметрические тесты")
print("Задача 4:\n\
Даны 3 группы учеников плавания. Не соблюдается условие нормальности.\n\
В 1 группе время на дистанцию 50 м составляют: \
56, 60, 62, 55, 71, 67, 59, 58, 64, 67\n\
Вторая группа: 57, 58, 69, 48, 72, 70, 68, 71, 50, 53\n\
Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54\n\
Есть ли статистически значимые различия между группами?\n")

α=0.05
time1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
time2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
time3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

print(f"Решение 4:\n\
Анализ независимых выборок, 3 группы данных.\n\
Выбран критерий Крускала-Уоллиса, α={α}.\n\
H0: статистически значимых различий нет\n\
H1: имеются статистически значимые различия\n")

print(stats.kruskal(time1, time2, time3))

statistic, pvalue = stats.kruskal(time1, time2, time3)
msg = 'H0 принимается, статистически значимых отличий нет' if α < pvalue \
    else 'H0 отвергается, принимается H1, есть статистически значимые отличия'
print(f'{msg}')