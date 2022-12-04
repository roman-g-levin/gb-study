while konf > 0:
    print(f'На столе {konf} конфет, у игроков: {pkonf}')
    if konf < 28:
        max_pget = konf
    else:
        max_pget = 28
    print(f'{player} может взять от 1 до {max_pget}')
    if player == 'человек':
        pget = int(input(f'Введите число конфет, которое взял {player}:'))
    else:
        pget = konf % 29    # хотим взять вот столько
        if pget < 1 or pget > max_pget:
            pget = random.randint(1, max_pget)  # если не можем взять сколько хотим, берем случайное число
        print(f'Бот взял {pget} конфет')
    if pget > max_pget or pget < 1:
        print('Неверный ввод')
        continue
    pkonf[player] += pget
    konf -= pget
    if player == 'человек':
        player = 'бот'
    else:
        player = 'человек'

print('Конфеты кончились')
if player == 'человек':
    player = 'бот'
else:
    player = 'человек'
print(f'Последнюю взял игрок {player}')
