import math

x = float(input("Please insert your value of x: "))
n_value = 10
temp = int(1)
answer = 0

for n in range(n_value):
    temp += 2
    sinx = ((-1) ** (n+1)) * (x ** temp) / math.factorial(temp)
    answer += sinx


print(answer)