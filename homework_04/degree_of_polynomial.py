# 33). Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k и приравняйте его к нулю.

from random import randrange

k = int(input())
pol = ''
while k != 0:
    ratio = randrange(0, 100)
    if ratio == 0:
        k -= 1
    elif ratio == 1:
        if k == 1:
            pol += f'x + {randrange(1, 100)} = 0'
        else:
            pol += f'x^{k} + '
    else:
        if k == 1:
            pol += f'{ratio}x + {randrange(1, 100)} = 0'
        else:
            pol += f'{ratio}x^{k} + '
    k -= 1
print(pol)




