health_points = int(input("Please enter your health points :"))

if health_points <= 0:
    is_dead = True
else:
    is_dead = False

if is_dead == True:
    print("Man is dead")
else:
    print("Man is Not Dead")
