import math

x = 1
num_terms = 100
estimate = 0

for n in range(num_terms):
    term= x**n / math.factorial(n)
    estimate += term

print(estimate)
