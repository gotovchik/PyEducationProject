
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def negafibonacci(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    return negafibonacci(n + 2) - negafibonacci(n + 1)


num = int(input("Enter the number: "))
col = list(range(-num, num + 1))
print(f'This is a list of numbers from -N to N:\n{col:}')

for i in range(len(col)):
    if col[i] > 0:
        col[i] = fibonacci(col[i])
    if col[i] < 0:
        col[i] = negafibonacci(col[i])

print(f'This is a list of Fibonacci sequence numbers for numbers from -N to N:\n{col}')



