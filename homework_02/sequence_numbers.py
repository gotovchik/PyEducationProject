"""
Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
"""


def get_sum_of_sequence(n):
    col = []
    for i in range(1, n + 1):
        col.append((1 + 1 / n) ** n)
    return sum(col)


number = int(input("Enter the number: "))
amount = get_sum_of_sequence(number)
print(amount)
