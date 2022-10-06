# 30. Вывести число pi с точностью d знаков после запятой


from math import pi, floor


def truncate(d):
    return floor(pi * 10 ** d) / 10 ** d


print('Привет!\nЭто программа выдаст вам число π с заданной вами точностью')
count = int(input('Введите точность d: '))
print(f'π = {truncate(count)}')

