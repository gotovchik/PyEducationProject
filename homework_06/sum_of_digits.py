"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
"""


# Было
def get_digits(num):
    col = []
    for ch in str(num):
        if ch.isdigit():
            col.append(int(ch))
    return col


number = float(input('Enter the real number: '))
digits1 = get_digits(number)
print(f'The amount of the digits of the number is {sum(digits1)}')

# Используя LC
digits2 = [int(i) for i in str(number) if i.isdigit()]
print(f'The amount of the digits of the number is {sum(digits2)}')
