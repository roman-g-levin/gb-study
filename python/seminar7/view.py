import model


def list_all(list_to_display=model.contacts):
    for i in list_to_display:
        print(f'Имя: {i["fio"]}, \tтел: {i["phone"]}')


# запрос записи
def get_contact(mode):
    fio = get_fio()
    phone = input('Введите телефон -> ')
    print(mode)
    print(f'Имя: {fio}, \tтел: {phone}')
    return (fio, phone)


# вывод результата удаления
def success(yes):
    if yes == 0:
        print('...неуспешно')
    else:
        print('...успешно')
    return


# запрос имени
def get_fio():
    fio = input('Введите имя -> ')
    return fio


# запрос имени файла и режима выгрузки
def get_export_format():
    filename = input('Введите имя файла -> ')
    type = input('Введите тип csv, txt или json -> ')
    return (filename,type)


# запрос имени файла для импорта
def get_import_filename():
    filename = input('Введите имя файла -> ')
    mode = input('0 - очистить справочник, 1 - добавить -> ')
    return (filename,mode)