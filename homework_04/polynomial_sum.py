# 34). Даны два файла, в каждом из которых находится запись многочлена,
# приравненного к нулю.
# Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).


# чтение файла
def read_file(file):
    with open(file, 'r') as data:
        return data.readlines()


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


# находим степени многочлена
def find_poly_degree(k):
    if 'x^' in k:
        i = k.find('^')
        degree = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        degree = 1
    else:
        degree = -1
    return degree


# находим коэффициенты многочлена
def find_coefficient(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


# разбор многочлена и получение его коэффициентов
def get_list_of_coefficient(poly):
    poly = poly[0].replace(' ', '').split('=')
    poly = poly[0].split('+')
    col = []
    f = len(poly)
    k = 0
    if find_poly_degree(poly[-1]) == -1:
        col.append(int(poly[-1]))
        f -= 1
        k = 1
    i = 1
    jj = f - 1
    while jj >= 0:
        if find_poly_degree(poly[jj]) != -1 and find_poly_degree(poly[jj]) == i:
            col.append(find_coefficient(poly[jj]))
            jj -= 1
            i += 1
        else:
            col.append(0)
            i += 1
    return col


# получаем суммы коэффициентов многочленов
def sum_poly(file1, file2):
    poly1 = read_file(file1)
    print(f'Первый многочлен: {poly1}')
    poly2 = read_file(file2)
    print(f'Второй многочлен: {poly2}')
    col1 = get_list_of_coefficient(poly1)
    col2 = get_list_of_coefficient(poly2)
    l = len(col1)
    if len(col1) > len(col2):
        l = len(col2)
    res = [col1[i] + col2[i] for i in range(l)]
    if len(col1) > len(col2):
        j = len(col1)
        for i in range(l, j):
            res.append(col1[i])
    else:
        j = len(col2)
        for i in range(l, j):
            res.append(col2[i])
    return res


path1 = 'file1.txt'
path2 = 'file2.txt'
res_poly = get_poly(sum_poly(path1, path2))
print(f'Сумма многочленов: {res_poly}')















