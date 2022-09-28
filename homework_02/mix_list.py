"""
Реализуйте алгоритм перемешивания списка.
"""
from random import randint


def shuffle_list(col):
    for i in range(len(col)):
        temp = col[i]
        r = randint(0, len(col) - 1)
        col[i] = col[r]
        col[r] = temp


def fill_list(count):
    col = []
    for i in range(0, count):
        col.append(randint(1, 100))
    return col


count_of_items = int(input("Enter the count of elements for the future list: "))
numbers = fill_list(count_of_items)
print(f'This is the list \n {numbers}')
shuffle_list(numbers)
print(f'This is the list after shuffling \n {numbers}')


