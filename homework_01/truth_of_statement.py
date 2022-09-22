# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

print('X Y Z Statement')
for X in range(2):
    for Y in range(2):
        for Z in range(2):
            var = not (X and Y and Z) == (not X or not Y or not Z)
            print(X, Y, Z, var)
