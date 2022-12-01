"""в этом файле описана модель, управление данными в модели
созранение и загрузка данных"""

employees = [
    {"id": 1, "fio": "ivan petrov", "salary": 40},
    {"id": 2, "fio": "bob ivanov", "salary": 50},
    {"id": 3, "fio": "john don", "salary": 100}
]

departments = [
    {"id": 100, "name": "accounting", "employees": [2, 1]},
    {"id": 101, "name": "marketing", "employees": [3]}
]


def add_department(name):
    """функция добавления отдела"""
    departments.append({
        "id": departments[-1]["id"] + 1,
        "name": name,
        "employees": []
    })
    save_base_to_csv()


def save_base_to_csv(filename='organisation.csv'):
    """функция записи всей базы отделов и сотрудников в файл"""
    with open(filename, 'w') as save:
        for i in employees:
            save.write('{};{};{}\n'.format(i["id"], i["fio"], i["salary"]))
        for i in departments:
            save.write('{};{};{}\n'.format(i["id"], i["name"], i["employees"]))

