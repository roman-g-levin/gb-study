from console_color import *

def display_field(a):
    """функция вывода игрового поля и подсказки"""
    print(' 7 | 8 | 9     ',end="")
    cprint(f' {a[7]} | {a[8]} | {a[9]} ', RGB.WHITE, RGB.BLUE)
    print('---+---+---    ',end="")
    cprint('---+---+---', RGB.WHITE, RGB.BLUE)
    print(' 4 | 5 | 6     ',end="")
    cprint(f' {a[4]} | {a[5]} | {a[6]} ', RGB.WHITE, RGB.BLUE)
    print('---+---+---    ',end="")
    cprint('---+---+---', RGB.WHITE, RGB.BLUE)
    print(' 1 | 2 | 3     ',end="")
    cprint(f' {a[1]} | {a[2]} | {a[3]} ', RGB.WHITE, RGB.BLUE)

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
            cprint('Ожидается ввод числа',RGB.RED,RGB.BLACK)
    

def display_message(msg):
    """функция вывода сообщения"""
    cprint(msg,RGB.RED,RGB.BLACK,Style.BOLD)
