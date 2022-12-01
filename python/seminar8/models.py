

employees = [
    {"id": 1, "fio": "ivan petrov", "salary": 40},
    {"id": 2, "fio": "bob ivanov", "salary": 50},
    {"id": 3, "fio": "john don", "salary": 100}
]

departments = [
    {"id": 10, "name": "accounting", "employees": [2, 1]},
    {"id": 11, "name": "marketing", "employees": [3]}
]


def add_department(name):
    # TODO: найти максимальный номер отдела и увеличить на 1
    departments.append({
        "id": departments[-1]["id"] + 1,
        "name": name,
        "employees": []
    })