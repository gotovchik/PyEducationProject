"""
23. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
o [2, 3, 4, 5, 6] => [12, 15, 16];
o [2, 3, 5, 6] => [12, 15]
"""
from math import ceil


def multiply_pairs(col):
    return [col[i] * col[-i - 1] for i in range(ceil(len(col) / 2))]


numbers = [2, 3, 4, 5, 6]
print(multiply_pairs(numbers))  # [12, 15, 16]
numbers.remove(4)
print(multiply_pairs(numbers))  # [12, 15]
