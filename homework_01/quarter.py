# 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
# o x=34; y=-30 -> 4
# o x=2; y=4-> 1
# o x=-34; y=-30 -> 3

def what_quarter(x, y):
    if x > 0 and y > 0:
        print('I четверть')
    elif x > 0 > y:
        print('IV четверть')
    elif x < 0 < y:
        print('II четверть')
    elif x < 0 and y < 0:
        print('III четверть')


A = int(input('Введите координату по оси Х:'))
B = int(input('Введите координату по оси Y:'))
what_quarter(A, B)
