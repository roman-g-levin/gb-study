
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
# Введите ваше решение ниже

backpack = []
goodies = []
weight = []

# раскидать справочник по спискам для удобства доступа по индексу
for i in items.items():
    #print(i[0],i[1])
    goodies.append(i[0])
    weight.append(i[1])
#print(goodies,weight)

# перебор всех возможных комбинаций вещей
for i in range(1,2**len(goodies)):
    # a - это генератор степени двойки для битового сравнения
    #a = (2**j for j in range(0,len(goodies)))
    workset = {}
    work_weight = 0.0
    # цикл по вещам
    for k in range(0,len(goodies)):        
        if i & 2**k:
            # эту вещь пытаемся добавить в набор
            if work_weight + weight[k] >= max_weight:
                # перевес
                continue
            work_weight += weight[k]
            workset[goodies[k]] = weight[k]
    #print(workset)
    if len(workset) > 0:
        backpack.append(workset)
   
print(backpack)