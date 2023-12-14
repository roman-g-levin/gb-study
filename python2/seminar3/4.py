# Введите ваше решение ниже
lst = [1, 1, 2, 2, 3, 3]
freq = {}
lst1 =[]

for i in lst:
    freq[i]=freq.get(i,0) + 1
#print(freq)

for i in freq.items():
    #print(i)
    if i[1] >= 2:
        lst1.append(i[0])

print(lst1)