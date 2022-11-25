﻿"""
Создать телефонный справочник с возможностью
импорта и экспорта данных в нескольких форматах.
(Применить MVC)

ТЗ:
Операции с телефонным справочником:
1. Вывод контактов
2. Добавление контакта ФИО и телефон
3. Удаление контакта
4. Поиск контакта по имени и вывести список найденных контактов
с заданным именем
5. Выгрузка в формате CSV, txt или JSON (экспорт)
6. Загрузка списка контактов из файлика выбранного формата
7. Редактирование контакта

Пример структуры:

contacts = [
{ "fio": "ivan petrov", "phone": "12345 },
{ "fio": "max petrov", "phone": "12333345 },
....
]
"""

import controller as c

# точка запуска программы
print('Программа работы с телефонным справочником')
# загрузка справочника из файла contacts.csv
c.load_contacts()

while True:
    print('Инструкция:')
    print('1 - вывод справочника')
    print('2 - добавление контакта')
    print('3 - удаление контакта')
    print('4 - поиск контакта по имени')
    print('5 - Выгрузка в формате CSV, txt или JSON')
    print('6 - Загрузка списка контактов из файла CSV')
    print('7 - Редактирование контакта')
    print('0 - Завершение работы')
    sel=int(input(f'--- введите команду ---> '))
    if sel==0:
        break
    elif sel==1:
        c.list_all()
    elif sel==2:
        c.add_contact()
    elif sel==3:
        c.del_contact()
    elif sel==4:
        c.find_by_name()
    elif sel==5:
        c.export_contacts()
    elif sel==6:
        c.import_contacts()
    elif sel==7:
        c.edit_contact()
    else:
        print('Некорретный ввод')
