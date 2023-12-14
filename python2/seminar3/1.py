#t='asd %.10f asd' % (200.0111)
#print(t)

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
# Введите ваше решение ниже

my_weight = 0.0
backpack = {}

for i in items:
    #print(i, items[i])
    if my_weight + items[i] >= max_weight:
        continue
    my_weight += items[i]
    backpack[i] = items[i]
    
print(backpack)
