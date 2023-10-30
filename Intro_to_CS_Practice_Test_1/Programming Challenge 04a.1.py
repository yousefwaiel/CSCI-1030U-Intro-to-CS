list1 = ["Apples", "Bannana", "Tomato", "Oranges"]
list2 = ["Red", "Yellow", "Red", "Orange"]
list3 = {}

for n in range(len(list1)):
    list3[list1[n]] = list2[n]

print(list3)
