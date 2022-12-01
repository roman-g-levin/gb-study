from models import add_department
from .ui_view import show_departments, show_employees, menu, show_employees_in_department, input_department

MENU_ACTIONS = {
    1: ["Вывести список отделов", show_departments],
    2: ["Вывести список всех сотрудников", show_employees],
    3: ["Вывести список сотрудников отдела (по номеру)", show_employees_in_department],
    4: ["Добавить отдел", input_department, add_department],
    5: ["Добавить сотрудника", lambda: print("todo")],
    6: ["Переместить сотрудника в другой отдел", lambda: print("todo")],
    7: ["Уволить сотрудника", lambda: print("todo")],
    # 8: ["Экспорт отделов в csv", export_deparments_to_csv],
    0: ["Выход", lambda: None]
}


def main():
    menu_number = 1000000

    while menu_number:
        menu_number = menu()
        input_data = MENU_ACTIONS[menu_number][1]()
        if input_data:
            MENU_ACTIONS[menu_number][2](input_data)
