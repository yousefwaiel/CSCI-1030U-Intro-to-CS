Mark = int(input("Please insert your mark out of 100: "))

if Mark <= 49:
    print("Your mark if F")
elif Mark <= 59:
    print("Your mark if D")
elif Mark <= 69:
    print("Your mark if C")
elif Mark <= 79:
    print("Your mark if B")
else:
    print("Your mark if A")
