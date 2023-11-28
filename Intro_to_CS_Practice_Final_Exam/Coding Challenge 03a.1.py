import math

x = float(input("Please insert your number "))
y = 100
n = 0
ans = 0

while y > 0:
    temp = ( pow(-1,n) / math.factorial(2*n+1) ) * pow(x, 2*n + 1)
    n += 1
    ans += temp
    y -=1

print(ans)