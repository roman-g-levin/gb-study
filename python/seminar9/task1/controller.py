from model import ARRAY
from view import menu, display_field, display_message


def main():
    PLAYER = 'X'
    global ARRAY
    while True:
        display_field(ARRAY)
        hod = menu(PLAYER)
        if hod == 0:
            break
        if ARRAY[hod] != ' ':
            display_message('Поле занято, повторите ввод\n')
            continue
        else:
            ARRAY[hod] = PLAYER
        if PLAYER == 'X':
            PLAYER = 'O'
        else:
            PLAYER = 'X'
        winner=win(ARRAY)
        if winner == '!':
            display_field(ARRAY)
            display_message(f'Игра окончена.\nНикто не выиграл.\n')
            break
        elif winner == ' ':
            continue
        else:
            display_field(ARRAY)
            display_message(f'Игра окончена!\nВыиграл игрок {winner}\n')
            break


def win(a):
    """функция возвращает символ выигравшего игрока,
    ' ' - пробел если выигрыша еще нет
    '!' если все поля заполнены без выигрыша"""
    empty=0
    for i in range(len(a)):
        if a[i]==' ':
            empty+=1
    if empty==1:
        return '!'
    if a[1] == a[2] and a[2] == a[3] and a[3] != ' ':
        return a[3]
    elif a[4] == a[5] and a[5] == a[6] and a[6] != ' ':
        return a[6]
    elif a[7] == a[8] and a[8] == a[9] and a[9] != ' ':
        return a[9]
    elif a[1] == a[4] and a[4] == a[7] and a[7] != ' ':
        return a[7]
    elif a[2] == a[5] and a[5] == a[8] and a[8] != ' ':
        return a[8]
    elif a[3] == a[6] and a[6] == a[9] and a[9] != ' ':
        return a[9]
    elif a[1] == a[5] and a[5] == a[9] and a[9] != ' ':
        return a[9]
    elif a[3] == a[5] and a[5] == a[7] and a[7] != ' ':
        return a[7]
    else:
        return ' '
