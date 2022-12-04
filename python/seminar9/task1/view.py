def display_field(a):
    """функция вывода игрового поля и подсказки"""
    print(f' {a[7]} | {a[8]} | {a[9]}      7 | 8 | 9')
    print('---+---+---    ---+---+---')
    print(f' {a[4]} | {a[5]} | {a[6]}      4 | 5 | 6')
    print('---+---+---    ---+---+---')
    print(f' {a[1]} | {a[2]} | {a[3]}      1 | 2 | 3')

def menu(player):
    while True:
        hod = input(f'Ход игрока {player}\nВведите номер поля от 1 до 9, 0 - выход:')
        if hod.isdigit():
            num=int(hod)
            if num>=0 and num<=9:
                return num
            else:
                continue
        else:
            print('Ожидается ввод числа')
    

def display_message(msg):
    """функция вывода сообщения"""
    print(msg)
