num1 = float(input("Please insert your first number"))
num2 = float(input("Please insert your second number"))

if num1%2 == 0 :
    num1T = True
else:
    num1T = False

if num2%2 == 0:
    num2T = True
else:
    num2T = False

if num1T == True & num2T == True:
    print("Both numbers are even")
else :
    print("Both numbers are NOT even ( odd )")