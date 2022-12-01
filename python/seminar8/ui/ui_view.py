from models import *
import ui.ui_controller

def show_departments():
    """функция вывода списка отделов"""
    print('Номер\tНазвание отдела')
    for department in departments:
        print(f' {department["id"]}\t{department["name"]}')


def show_employees():
    """функция вывода списка сотрудников"""
    print('Номер\tСотрудник\tЗарплата')
    for employee in employees:
        print(f' {employee["id"]}\t{employee["fio"]}\t{employee["salary"]}')
       

def show_employees_in_department():
    """функция вывода списка сотрудников отдела по номеру отдела"""
    department_id = int(input("Введите id отдела: "))
    flag_not_found=True
    for department in departments:
        if department["id"] == department_id:
            flag_not_found=False
            print(f'Список сотрудников отдела {department["name"]}')
            print('Номер\tСотрудник\tЗарплата')
            for employee in department["employees"]:
                empl = [e for e in employees if e["id"]==employee]
                print(empl)
                #print(f' {empl[0]["id"]}\t{empl[0]["fio"]}\t{empl[0]["salary"]}')
            break
    if flag_not_found:
        print(' Не найден номер отдела!')


def menu():
    for key, item in ui.ui_controller.MENU_ACTIONS.items():  # [(1, "..."), (2, "....")... ]
        print(key, item[0])

    return int(input("Выберите пункт меню: "))


def input_department():
    return input("Введите название отдела: ")


def display_message(txt):
    """функция вывода текста"""
    print(txt)

