def get_divisors(num):
    return sum([num % x == 0 for x in range(1, num + 1)])