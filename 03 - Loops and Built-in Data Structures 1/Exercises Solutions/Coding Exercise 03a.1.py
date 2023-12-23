import math

x = float(input("Please insert your number "))
n = 0
ans = 0
y = 100
while y > 0 :
    temp = (pow(x,n))/ math.factorial(n)
    ans += temp
    n += 1
    y -=1

print(ans)