def fib(n):
    # base case
    if n == 0 or n == 1:
        return n

        # recursive case
    return fib(n - 1) + fib(n - 2)

print(f'{fib(0) = }')
print(f'{fib(1) = }')
print(f'{fib(2) = }')
print(f'{fib(3) = }')
print(f'{fib(4) = }')
print(f'{fib(11) = }')