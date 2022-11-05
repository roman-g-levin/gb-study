"""
Создайте программу для игры в ""Крестики-нолики"".
"""

# объявление функций и методов


def display(a):
    print(f' {a[1]} | {a[2]} | {a[3]}      1 | 2 | 3')
    print('---+---+---    ---+---+---')
    print(f' {a[4]} | {a[5]} | {a[6]}      4 | 5 | 6')
    print('---+---+---    ---+---+---')
    print(f' {a[7]} | {a[8]} | {a[9]}      7 | 8 | 9')


def win(a):
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


# начало программы
print('Программа игры в крестики-нолики. Нумерация полей:')
print(' 1 | 2 | 3')
print('---+---+---')
print(' 4 | 5 | 6')
print('---+---+---')
print(' 7 | 8 | 9\n')

array = [" " for i in range(10)]
player = 'X'

while win(array) == ' ':
    display(array)
    print(f'Ход игрока {player}')
    hod = int(input(f'Введите номер поля:'))
    if hod < 1 or hod > 9:
        print('Неверный номер поля')
        continue
    if array[hod] != ' ':
        print('Поле занято, повторите ввод')
        continue
    else:
        array[hod] = player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

display(array)
print(f'Выиграл игрок {win(array)}')
