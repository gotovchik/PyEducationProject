"""
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.
Пример:
o [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
from math import floor


def truncate(num):  # обрезаем хвост без округления
    return floor(num * 10 ** 2) / 10 ** 2


def get_diff(mylist):
    max_fp = 0
    min_fp = 1
    for i in mylist:
        if i - int(i) >= max_fp:
            max_fp = i - int(i)
        if i - int(i) <= min_fp:
            min_fp = i - int(i)
    diff = max_fp - min_fp
    return truncate(diff)


nums = [1.1, 1.2, 3.1, 5, 10.01]
print(f'This is the number list:\t{nums}')
print(f'The difference between the maximum and minimum factional parts is\t{get_diff(nums)}')


