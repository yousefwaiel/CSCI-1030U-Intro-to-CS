import math


def math1(x, n, max_n):
    total = 0.0

    for i in range(n, max_n + 1):
        term = math.pow(-1, i) * pow(x, i) / math.factorial(i)
        total += term

    return total


print(math1(0.5, 0, 10))
