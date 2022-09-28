"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""
from math import factorial


def get_numbers(n):
    nums = []
    for i in range(1, n + 1):
        nums.append(factorial(i))
    return nums


num = int(input('Enter the number:'))
numbers = get_numbers(num)
print(f"Set of number's multiply: {numbers}")






