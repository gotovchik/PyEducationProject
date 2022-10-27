"""
9. Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y)

"""


def coordinates(n):
    if n == 1:
        print('x > 0, y > 0')
    elif n == 2:
        print('x < 0 < y')
    elif n == 3:
        print('x < 0, y < 0')
    elif n == 4:
        print('x > 0 > y')
    else:
        print('Введен не верный номер четверти.')


number_of_quarter = int(input('Введите номер четверти: '))
coordinates(number_of_quarter)
