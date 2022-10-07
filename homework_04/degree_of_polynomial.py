# 33). Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k и приравняйте его к нулю.

from random import randrange


def get_polynomial(k):
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
    return pol


def write_to_file(file, x):
    with open(file, 'w') as data:
        data.write(x)


def read_file(file):
    with open(file, 'r') as data:
        print(data.read())


degree = int(input('Введите степень первого многочлена:'))
polynomial = get_polynomial(degree)
path = 'file1.txt'
write_to_file(path, polynomial)
read_file(path)

degree2 = int(input('Введите степень второго многочлена:'))
polynomial2 = get_polynomial(degree2)
path2 = 'file2.txt'
write_to_file(path2, polynomial2)
read_file(path2)





