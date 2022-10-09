"""
2. Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.
"""

print('Программа для проверки истинности логического утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
LogicalSet = [False, True]
for X in LogicalSet:
    for Y in LogicalSet:
        for Z in LogicalSet:
            print(f'¬({X} ⋁ {Y} ⋁ {Z}) = ¬{X} ⋀ ¬{Y} ⋀ ¬{Z} - ', end="")
            if (not (X or Y or Z)) == (not X and not Y and not Z):
                print('истина')
            else:
                print('ложь')
