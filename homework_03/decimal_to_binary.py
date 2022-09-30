"""
25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
 45 -> 101101
 3 -> 11
 2 -> 10
"""
from numpy import binary_repr

# use numpy

print(binary_repr(45), end=" ")  # 101101
print(binary_repr(3), end=" ")  # 11
print(binary_repr(2), end=" ")  # 10
print()

# use string format

print(f'{45:b}', end=" ")  # 101101
print(f'{3:b}', end=" ")  # 11
print(f'{2:b}', end=" ")  # 10
print()

# use bin()

print(int(bin(45)[2:]), end=" ")  # 101101
print(int(bin(3)[2:]), end=" ")  # 11
print(int(bin(2)[2:]), end=" ")  # 10
print()


