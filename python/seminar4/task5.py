"""
Даны два файла, в каждом из которых
 находится запись многочлена. Задача - 
сформировать файл, содержащий сумму многочленов.
"""
# функция выделения степени и коэффициента из строки
def get_k(str):
    #print(f'str:{str}')
    ind=str.find('*x**')
    if ind==(-1):
        #считаем, что степень 0
        k=int(str)
        pow=0
    else:
        k=int(str[:ind])
        pow=int(str[ind+4:])
    #print(f'ind:{ind}, k:{k}, pow:{pow}')
    return {pow:k}

# функция выделения коэффициентов многочлена из строки
def k_to_dict(s):
    res={}
    str_splitted=s.split('+')
    #print(f'{str_splitted}')
    for str in str_splitted:
        pow_k=get_k(str)
        res.update(pow_k)
    return res

array=[]
print('Программа сложения многочленов из файлов')
print('Из-за невнятного задания и моей лени обрабатываются только положительные коэффициенты')
data=open('task4.txt','r')
for line in data:
    array.append(line)
data.close()
data=open('task5.txt','r')
for line in data:
    array.append(line)
data.close()

print('Считаны из файлов многочлены:')
print(array)

print('Выделены коэффициенты многочленов:')
for str in array: 
    print(k_to_dict(str))

# определение максимальной степени многочлена
max_k=[]
for str in array:
    max_k.append(max(*k_to_dict(str).keys()))
k=max(max_k)

# сложение коэффициентов
result=[0 for i in range(k+1)]
for str in array:
    this_dict=k_to_dict(str)
    for i in range(k+1):
        result[i]+=this_dict.get(i,0)

# вывод многочлена
print('Результирующий многочлен:')
for i in range(k,0,-1):
    print(f'{result[i]}*x**{i} + ',end='')
print(f'{result[0]}')
