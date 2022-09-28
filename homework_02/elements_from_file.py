"""
Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции (случайные) хранятся в файле file.txt
(создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
"""
from random import randint
import os


def get_multiply_of_elements_from_file(arr, path):
    result = 1
    print('Elements for product:', end=' ')
    data = open(path, 'r')
    for line in data:
        print(arr[int(line)], end=', ')
        result *= arr[int(line)]
    data.close()
    return result


def get_collection(n):
    return list(range(-n, n + 1))


def fill_file(path, lines_count, maximum):
    data = open(path, 'w')
    for i in range(1, lines_count + 1):
        data.write(str(randint(0, maximum)) + "\n")
    data.close()


p = 'file.txt'
number = int(input('Enter the number: '))
col = get_collection(number)
print(*col)
count = int(input("Enter the count of numbers to be multiplied: "))
fill_file(p, count, len(col) - 1)
product = get_multiply_of_elements_from_file(col, p)
print(f'the product of the elements numbered from the file is {product}')
os.remove(p)
