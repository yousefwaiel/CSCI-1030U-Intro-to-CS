age = int(input("Please insert your age "))

try:
    if age < 18:
        raise Exception
    print(f"You're {age} years old")
except Exception:
    print("You're not 18 yet, grow up")