import math
from random import randint

x = float(input("Please insert your number value :"))

y = math.sqrt(x)

z = 0

temp = 0

while z != y:
    if y > z:
        temp += 1
        z = math.sqrt(temp)
    else:
        temp -= 1
        z = math.sqrt(temp)

print("The square root of the number you inserted is ", z)
