
full_name = str(input("Please insert your first and last name with a space in between: "))

temp = full_name.split()

first_name = temp[0]
last_name = temp[1]

print("Your first name is", first_name)
print("Your last name is", last_name)