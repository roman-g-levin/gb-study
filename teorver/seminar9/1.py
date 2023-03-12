import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

print("Теория вероятностей и математическая статистика")
print("Семинар 9. Линейная регрессия Логистическая регрессия")
print("Задача 1:\n\
Даны значения величины заработной платы заемщиков банка (zp) \
и значения их поведенческого кредитного скоринга (ks): \n\
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], \n\
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].\n\
Используя математические операции, посчитать коэффициенты \
линейной регрессии, приняв за X заработную плату (то есть, \
zp - признак), а за y - значения скорингового балла (то есть, \
ks - целевая переменная). Произвести расчет как с использованием \
intercept, так и без.")

# списки
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
x = np.array(zp)
y = np.array(ks)

# длина списка
n=len(x)

# отобразим исходные точки на графике
plt.scatter(x,y)

# y = a + bx, поиск математическим методом
b=(n * sum(x*y) - sum(x)*sum(y)) / (n * sum(x**2) - sum(x)**2)
a=np.mean(y) - b*np.mean(x)
plt.plot(x, b * x + a, 'g')
print(f'Решение 1.1 математическим методом\n\
y = a + x*b: coef (b)={b}, intercept (a)={a}\n')
plt.title('1.1 Поиск решения Математическим методом y = a + b*x')
plt.show()

# поиск решения матричным методом
Y=y.reshape(-1, 1)
X2=x.reshape(-1, 1)
X1=np.hstack([np.ones((n,1)),X2])
# с интерсептом
B1=np.linalg.inv( np.transpose(X1).dot(X1) ).dot(np.transpose(X1)).dot(Y)
b0_1 = B1[0][0]
b1_1 = B1[1][0]
# без интерсепта
B2=np.linalg.inv( np.transpose(X2).dot(X2) ).dot(np.transpose(X2)).dot(Y)
b1_2 = B2[0][0]

# показать результат
plt.scatter(x,y)
plt.plot(x, b1_1 * x + b0_1, 'g')
plt.plot(x, b1_2 * x, 'r')
print(f'Решение 1.2 матричным методом\n\
С интерсептом: coef={b1_1}, intercept={b0_1}\n\
Без интерсепта: coef={b1_2}, intercept={0}\n')
plt.title('1.2 Поиск решения матричным методом с интерсептом и без')
plt.show()

# Линейная регрессия через библиотеку
# reshape
x_= x.reshape(-1, 1)
y_= y.reshape(-1, 1)
# с интерцептом
model_with_i = LinearRegression(fit_intercept=True).fit(x_, y_)
const1 = model_with_i.intercept_
beta1 = model_with_i.coef_[0]
plt.plot(x_, beta1 * x_ + const1, 'g')
# без интерцепта
model_without_i=LinearRegression(fit_intercept=False).fit(x_, y_)
const2 = model_without_i.intercept_
beta2 = model_without_i.coef_[0]
plt.plot(x_, beta2 * x_ + const2, 'r')
# вывод результата
print(f'Решение 1.3 через LinearRegression()\n\
С интерсептом: coef={beta1}, intercept={const1}\n\
Без интерсепта: coef={beta2}, intercept={const2}')
# отобразим исходные точки на графике
plt.scatter(x,y)
plt.title('1.3 Поиск решения через LinearRegression() с интерсептом и без')
plt.show()
