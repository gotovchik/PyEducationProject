# 7. Показать числа от -N до N

n = int(input('Введите N:'))

# print(*range(-n, n+1))

numbers = range(-n, n+1)
for i in numbers:
    print(i)

