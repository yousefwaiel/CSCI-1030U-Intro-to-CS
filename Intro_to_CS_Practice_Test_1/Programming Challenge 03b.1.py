num_list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 0]
even_list = []
temp = 0

for n in num_list:
    if n % 2 == 0:
        even_list.append(n)


average_num_list = sum(even_list) / len(even_list)

print("The average of the even numbers in the list is:", average_num_list)
