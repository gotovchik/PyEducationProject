"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
"""


def get_digits(num):
    col = []
    for ch in str(num):
        if ch == '.':
            continue
        else:
            col.append(int(ch))
    return col


number = input('Enter the real number: ')
digits = get_digits(number)
print(f'The amount of the digits of the number is {sum(digits)}')





