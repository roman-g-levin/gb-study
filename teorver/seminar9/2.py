import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

print("Теория вероятностей и математическая статистика")
print("Семинар 9. Линейная регрессия Логистическая регрессия")
print("Задача 2:\n\
Посчитать коэффициент линейной \
регрессии при заработной плате \
(zp), используя градиентный спуск \
(без intercept).")

# списки
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
x = np.array(zp)
y = np.array(ks)

# длина списка
n=len(x)

# поиск b1 (y = b1*x) методом градиентного спуска
# задать точность поиска
precition = 1e-5
# задать стартовую точку
b1 = 100.0001
# сохраняем предыдущее значение для досрочного выхода из цикла
b1_=b1

for i in range(1000):
    b1 -= precition * (2/n)*np.sum((b1*x - y) * x)
    if abs(b1 - b1_) < precition:
        break
    b1_=b1
    print(f'Итерация: {i}, значение b1:{b1}')

print(f'Решение 2. y = b1*x\n\
Без интерсепта: coef (b1)={b1}')
# отобразим исходные точки на графике
plt.scatter(x,y)
plt.plot(x, b1*x, 'r')
plt.title('2. Поиск решения без интерсепта градиентным спуском')
plt.show()
