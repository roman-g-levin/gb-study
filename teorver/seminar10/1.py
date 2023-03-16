import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
import pandas as pd

print("Теория вероятностей и математическая статистика")
print("Семинар 10. Дисперсионный анализ")
print("Задача 1:\n\
Провести дисперсионный анализ для определения того, есть ли различия \
среднего роста среди взрослых футболистов, хоккеистов и штангистов. \
Даны значения роста в трех группах случайно выбранных спортсменов:\n\
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.\n\
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.\n\
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.\n")

# списки
f = [173, 175, 180, 178, 177, 185, 183, 182]
h = [177, 179, 180, 188, 177, 172, 171, 184, 180]
sh = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]
x = np.array(f)
y = np.array(h)
z = np.array(sh)

# количество элементов в списках
nx=len(x)
ny=len(y)
nz=len(z)

# вычисляем среднее значение по группам
Mx=np.mean(x)
My=np.mean(y)
Mz=np.mean(z)

# координата Х для отображения выборок на графике
xx=[]
for i in range(nx):
    xx.append(1)
xy=[]
for i in range(ny):
    xy.append(2)
xz=[]
for i in range(nz):
    xz.append(3)

# отобразим исходные выборки на графике
plt.scatter(xx,x)
plt.scatter(xy,y)
plt.scatter(xz,z)

# отобразим средние значения
plt.plot(np.array([0.75,1.25]), np.array([Mx,Mx]), 'b')
plt.plot(np.array([1.75,2.25]), np.array([My,My]), 'r')
plt.plot(np.array([2.75,3.25]), np.array([Mz,Mz]), 'g')
plt.title(f'Распределение роста по Футболистам (Mx={Mx}),\nХоккеистам (My={My}) и\nШтангистам (Mz={Mz})')

# проверка на наличие статистически значимых различий в группах
alpha=0.05
f=stats.f_oneway(x,y,z)
if f.pvalue>=alpha:
    print('Отсутствуют статистически значимые различия средних значений роста в группах\n')
else:
    print('Имеются статистически значимые различия средних значений роста в группах\n')

    # ищем различия
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    # подготовка датафрейма pandas
    dfx=pd.DataFrame({
        'high': x,
        'sport': np.repeat(['football'],repeats=nx)
    })
    dfy=pd.DataFrame({
        'high': y,
        'sport': np.repeat(['hockey'],repeats=ny)
    })
    dfz=pd.DataFrame({
        'high': z,
        'sport': np.repeat(['shtanga'],repeats=nz)
    })
    df = pd.concat([dfx, dfy, dfz])

    # ищем различия тестом Тьюки
    tukey=pairwise_tukeyhsd(endog=df['high'],groups=df['sport'], alpha=alpha)
    print(tukey)
    print('Тест показывает наличие статистически значимого отличия среднего группы штангистов')

# вывести график
plt.show()
