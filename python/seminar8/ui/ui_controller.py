from models import add_department, del_department, load_base_from_csv, add_user
from .ui_view import show_departments, show_employees, menu, show_employees_in_department, input_department, input_no_department, input_username_and_other

MENU_ACTIONS = {
    1: ["Вывести список отделов", show_departments],
    2: ["Вывести список всех сотрудников", show_employees],
    3: ["Вывести список сотрудников отдела (по номеру)", show_employees_in_department],
    4: ["Добавить отдел", input_department, add_department],
    5: ["Удалить отдел", input_no_department, del_department],
    6: ["Добавить сотрудника", input_username_and_other, add_user],
    7: ["Переместить сотрудника в другой отдел", lambda: print("todo")],
    8: ["Удалить сотрудника", lambda: print("todo")],
    0: ["Выход", lambda: None]
}


def main():
    load_base_from_csv()
    menu_number = 1000000
    while menu_number:
        menu_number = menu()
        input_data = MENU_ACTIONS[menu_number][1]()
        if input_data:
            MENU_ACTIONS[menu_number][2](input_data)

