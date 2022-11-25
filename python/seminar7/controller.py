import model
import view
import os.path


# чтение справочника из файла csv
def load_contacts(filename='contacts.csv', clear=True):
    if os.path.isfile(filename):
        if clear:
            model.contacts.clear()
        rd = open(filename, 'r')
        for line in rd:
            spline = line.split(';')
            new_record = {"fio": spline[0], "phone": spline[1].rstrip()}
            model.contacts.append(new_record)
        rd.close()


def save_contacts(filename='contacts.csv'):
    with open(filename, 'w') as save:
        for i in model.contacts:
            save.write('{};{}\n'.format(i["fio"], i["phone"]))


# 1 - вывод всех контактов
def list_all():
    view.list_all()

# 2 - добавление контакта


def add_contact():
    fio, phone = view.get_contact('Добавлен абонент:')
    new_record = {"fio": fio, "phone": phone}
    model.contacts.append(new_record)
    with open('contacts.csv', 'a') as add:
        add.write('{};{}\n'.format(fio, phone))


def del_contact():
    fio, phone = view.get_contact('Удаляю абонента:')
    for i in range(len(model.contacts)):
        if model.contacts[i]["fio"] == fio and model.contacts[i]["phone"] == phone:
            yes = 1
            model.contacts.pop(i)
            break
        else:
            yes = 0
    view.success(yes)
    if yes == 1:
        save_contacts()
        


def find_by_name():
    temp_list = []
    fio = view.get_fio()
    for i in model.contacts:
        if i["fio"] == fio:
            temp_list.append(i)
    view.list_all(temp_list)


# экспорт справочника
def export_contacts():
    filename, type = view.get_export_format()
    fname=filename+'.'+type
    if type=='csv':
        save_contacts(fname)
    elif type=='txt':
        with open(fname, 'w') as save:
            for i in model.contacts:
                save.write('{},\t{}\n'.format(i["fio"], i["phone"]))
    elif type=='json':
        with open(fname, 'w') as save:
            save.write('[\n')
            first_entry=1
            for i in model.contacts:
                if first_entry==1:
                    first_entry=0
                else:
                    save.write(',\n')
                save.write('  {\n')
                save.write('    "fio": "{}",\n'.format(i["fio"]))
                save.write('    "phone": "{}"\n'.format(i["phone"]))
                save.write('  }')
            save.write('\n]\n')


#импорт справочника
def import_contacts():
    fname, mode = view.get_import_filename()
    if mode=='0':
        mode=True
    else:
        mode=False
    load_contacts(filename=fname, clear=mode)
    save_contacts()
    return


def edit_contact():
    fio, phone = view.get_contact('Редактирование контакта')
    for i in model.contacts:
        if i["fio"] == fio and i["phone"] == phone:
            new_fio, new_phone = view.get_contact('Измененные данные:')
            i["fio"] = new_fio
            i["phone"] = new_phone
            break
    save_contacts()
    return