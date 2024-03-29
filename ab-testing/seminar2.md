﻿# Решение ДЗ семинара 2
## A/B-тестирование

### Задание 1.
Сделайте приоритезацию гипотез из предыдущего урока с помощью ICE

### Решение:
Гипотезы из прошлого домвшнего задания:
1. Если применить более сложные модели прогнозирования и повысить точность средне- и долгосрочных прогнозов до уровня 0,95%, то в течение 3 лет можно ожидать увеличения количества российских пользователей в 1,5 раза.
2. Если отказаться от желтых агрегаторов новостей (с низкой репутацией и качеством контента) и брать ленту с профессиональных информационных агентств, это поднимет репутацию сайта и повысит количество кликов по новостям на 10%.
3. Если уменьшить размер стандартного рекламного блока на 1/3, то можно увеличить количество рекламных показов с 5 до 7 на странице и за счет этого увеличить количество переходов на 5%.
4. Если добавить на страницу прогноза карту региона клиента с анимацией, это повысит заинтересованность клиентов и увеличит среднее время пребывания на сайте на 10%.
5. Если добавить на страницу прогноза информационную сводку по истории наблюдений, это увеличит среднее время пребывания на сайте на 10%.

Сводная таблица ICE скоринга:

| Идея | Impact (0...10) | Confidence (0...10) | Ease (0...10) | ICE (I*C*E) |
|:----:|:---------------:|:-------------------:|:-------------:|:------:|
|1|5|5|1|25|
|2|5|0.1|9|4.5|
|3|5|0.1|10|5|
|4|5|3|4|60|
|5|5|3|5|75|

Наивысший результат по ICE-скорингу у гипотезы 5.

### Задание 2.
Составьте шаблон дизайна эксперимента для гипотезы, которая набрала больше всего баллов в практическом задании предыдущего урока

### Решение
1. Гипотеза:
"Если добавить на страницу прогноза информационную сводку по истории наблюдений, это увеличит среднее время пребывания на сайте на 10%."
2. Что делаем:
Добавляем на страницу с текущим прогнозом погоды историческую справку по параметрам климата за последние 25 лет в табличном виде. Также добавляем сведения по экстремальным значениям параметров погоды на текущую дату за всю историю наблюдений.
3. На каких пользователях тестируем:
Случайным образом выбираем из потока пользователей 50% распределения по запрашиваемому региону и направляем на модифицированный сервис. Остальные 50% посетителей оставляем на прежней версии сервиса.
4. Ключевые метрики для оценки эксперимента:
Ключевая метрика - время пребывания пользователя на сайте. Вторичные метрики: количество переходов по рекламе и новостным ссылкам.
5. Ожидаемый эффект:
Ожидаемый эффект - увеличение среднего времени нахождения пользователя на сайте на 10%. Желаемый эффект - увеличение количества переходов по рекламе и новостным ссылкам.
6. План действий в зависимости от результатов эксперимента:
При достижении ожидаемого эффекта и отсутствия снижения вторичных метрик, внедряем изменения для 100% посетителей сервиса. При отсутствии ожидаемого эффекта или при снижении вторичных метрик возвращаем функционал сервиса с изначальному состоянию.

