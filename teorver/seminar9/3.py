import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

print("Теория вероятностей и математическая статистика")
print("Семинар 9. Линейная регрессия Логистическая регрессия")
print("Задача 3:\n\
(Дополнительно). Произвести вычисления \
как в пункте 2, но с вычислением \
intercept. Учесть, что изменение \
коэффициентов должно производиться \
на каждом шаге одновременно (то \
есть изменение одного коэффициента \
не должно влиять на изменение \
другого во время одной итерации).")

# списки
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
x = np.array(zp)
y = np.array(ks)

# длина списка
n=len(x)

# поиск b1 и b0 (y = b0 + b1*x) методом градиентного спуска
# задать точность поиска
precition1 = 1e-7
precition0 = 1e-3
# задать стартовую точку
b1 = 0
b0 = 0
# сохраняем предыдущее значение для досрочного выхода из цикла
b1_=b1
b0_=b0
#mse_=mse(b1, b0, y, x, n)

#def mse(b1=b1, b0=b0, y=y, x=x, n=n):
#    return np.sum((y-(b1*x+b0))**2)/n
#mse_=mse(b1, b0, y, x, n)

for i in range(100000):
    b1 -= precition1 * (2/n)*np.sum(((b1*x + b0) - y) * x)
    b0 -= precition0 * (2/n)*np.sum(((b1*x + b0) - y) * 1)
    if (abs(b1 - b1_) < precition1) and (abs(b0 - b0_) < precition0):
        break
    b1_=b1
    b0_=b0
 #   mse_=mse(b1, b0, y, x, n)
    if i%100 == 0:
        print(f'Итерация {i}: b1={b1}, b0={b0}')

print(f'Решение 3. y = b0 + b1*x\n\
С интерсепом: coef (b1)={b1}, interceipt (b0)={b0}')
# отобразим исходные точки на графике
plt.scatter(x,y)
plt.plot(x, b1*x + b0, 'r')
plt.title('3. Поиск решения с интерсептом градиентным спуском')
plt.show()
