"""
Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции (случайные) хранятся в файле file.txt
(создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
"""
import random


def get_multiply_of_elements_from_file(arr, path):
    result = 1
    data = open(path, 'r')
    for line in data:
        result *= arr[int(line)]
    return result


def get_collection(n):
    return list(range(-n, n + 1))


def fill_file(path, lines_count, maximum):
    f = open(path, 'w')
    for i in range(1, lines_count + 1):
        f.write(str(random.randint(0, maximum)) + "\n")


p = 'file.txt'
number = int(input('Enter the number: '))
count = int(input("Enter the count of numbers to be multiplied: "))
col = get_collection(number)
fill_file(p, count, len(col) - 1)
product = get_multiply_of_elements_from_file(col, p)
print(f'The product of the elements numbered from the file is {product}')





