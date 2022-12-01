from models import *
import ui.ui_controller

def show_departments():
    """функция вывода списка отделов"""
    print('Номер\tНазвание отдела')
    for department in departments:
        print(f' {department["id"]}\t{department["name"]}')


def show_employees():
    """функция вывода списка сотрудников"""
    print('Номер\tСотрудник')
    for employee in employees:
        print(f' {employee["id"]}\t{employee["fio"]}')
       

def show_employees_in_department():
    department_id = int(input("Введите id отдела: "))
    # TODO: обработка случая, если id отдела некорректный
    department = [d for d in departments if d["id"] == department_id][0]
    print("empolyees ids: ", department["employees"])


def menu():
    for key, item in ui.ui_controller.MENU_ACTIONS.items():  # [(1, "..."), (2, "....")... ]
        print(key, item[0])

    return int(input("Выберите пункт меню: "))


def input_department():
    return input("Введите название отдела: ")
