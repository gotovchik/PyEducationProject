"""
Площадь прямоугольника — это произведение его длины
на его ширину. Напишите программу, которая запрашивает длину и ширину двух прямоугольников.
Программа должна выводить пользователю сообщение о том,
площадь какого прямоугольника больше, либо сообщать, что они одинаковы.
"""


def what_area_is_largest(length1, width1, length2, width2):
    square1 = length1 * width1
    square2 = length2 * width2

    if square1 > square2:
        print('The area of the first rectangle is larger than the second one')
    elif square2 > square1:
        print('The area of the second rectangle is larger than the first one')
    else:
        print('Rectangles an equal')


l1 = int(input('Enter the length of the first rectangle: '))
w1 = int(input('Enter the width of the first rectangle: '))

l2 = int(input('Enter the length of the second rectangle: '))
w2 = int(input('Enter the width of the second rectangle: '))

what_area_is_largest(l1, w1, l2, w2)




