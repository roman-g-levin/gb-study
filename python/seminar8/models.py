"""в этом файле описана модель, управление данными в модели
созранение и загрузка данных"""
import os.path

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

def load_base_from_csv(filename='organisation.csv'):
    """чтения всей базы отделов и сотрудников из файла"""
    if os.path.isfile(filename):
        employees.clear()
        departments.clear()
        rd = open(filename, 'r')
        for line in rd:
            spline = line.split(';')
            if int(spline[0])<100:
                new_record = new_record = {"id": int(spline[0]), "fio": spline[1], "salary": int(spline[2].rstrip())}
                employees.append(new_record)
            else:
                new_record = {"id": int(spline[0]), "name": spline[1], "employees": spline[2].rstrip()}
                departments.append(new_record)
        rd.close()
    print(departments)
    print(employees)
