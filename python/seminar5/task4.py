"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

# объявление функций и методов
def compress(s):
    if len(s)==0:
        return ''
    ch = s[0]
    i = 1
    if len(s) < 10:
        lim = len(s)
    else:
        lim = 10
    for i in range(1, lim):
        if s[i] != ch:
            break
    return ch+str(i)+compress(s[i:])

def decompress(s):
    if len(s)==0:
        return ''
    return s[0]*int(s[1])+decompress(s[2:])

# начало программы
print('Программа реализации RLE-алгоритма')
print('Сжатие:')
path_in = 'task4_in.txt'
path_out = 'task4_out.txt'
data = open(path_in, 'r')
dataout = open(path_out, 'w')
for line in data:
    print(f'{line.rstrip()} -> {compress(line.rstrip())}')
    dataout.write(compress(line.rstrip())+'\n')
data.close()
dataout.close()

print('Распаковка:')
path_in = 'task4_out.txt'
data = open(path_in, 'r')
for line in data:
    print(f'{line.rstrip()} -> {decompress(line.rstrip())}')
data.close()
