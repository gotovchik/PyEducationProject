# 33). Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k и приравняйте его к нулю.

from random import randint


# создаем список коэффициентов
def get_coefficient(k):
    return [randint(0, 101) for i in range(k + 1)]


# запись многочлена в виде строки
def get_poly(col):
    col = col[::-1]
    poly = ""
    if len(col) < 1:
        poly = "x = 0"
    else:
        for i in range(len(col)):
            if i != len(col) - 1 and col[i] != 0 and i != len(col) - 2:
                poly += f'{col[i]}x^{len(col) - i - 1}'
                if col[i+1] != 0 or col[i+2] != 0:
                    poly += ' + '
            elif i == len(col) - 2 and col[i] != 0:
                poly += f'{col[i]}x'
                if col[i+1] != 0 or col[i+2] != 0:
                    poly += ' + '
            elif i == len(col) - 1 and col[i] != 0:
                poly += f'{col[i]} = 0'
            elif i == len(col) - 1 and col[i] == 0:
                poly += " = 0"
    return poly


# запись в файл
def write_to_file(file, x):
    with open(file, 'w') as data:
        data.write(x)


# чтение файла
def read_file(file):
    with open(file, 'r') as data:
        return data.readlines()


degree = int(input('Введите степень первого многочлена:'))
polynomial = get_poly(get_coefficient(degree))
path = 'file1.txt'
write_to_file(path, polynomial)
print(read_file(path))

degree2 = int(input('Введите степень второго многочлена:'))
polynomial2 = get_poly(get_coefficient(degree2))
path2 = 'file2.txt'
write_to_file(path2, polynomial2)
print(read_file(path2))

