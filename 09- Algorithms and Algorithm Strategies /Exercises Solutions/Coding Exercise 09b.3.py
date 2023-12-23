def dp_fib(n):
    solutions = [0, 1]

    if n < 2:
        return solutions[n]

    for i in range(2, n + 1):
        next_fib = solutions[i - 1] + solutions[i - 2]
        solutions.append(next_fib)

    return solutions[n]


print(f'{dp_fib(0) = }')
print(f'{dp_fib(1) = }')
print(f'{dp_fib(2) = }')
print(f'{dp_fib(3) = }')
print(f'{dp_fib(4) = }')
print(f'{dp_fib(120) = }')