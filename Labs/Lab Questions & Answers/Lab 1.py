# Part 1

cost_per_item = float(input("Please insert the cost of the item : $"))
quantity = float(input("Please insert the quantity : $"))

subtotal_cost = cost_per_item * quantity

tax = subtotal_cost * 0.13

total_cost = tax + subtotal_cost

print(total_cost)

# Part 2

print("cost_per_item = " + str(cost_per_item))
print("quantity = " + str(quantity))
print("subtotal_cost = " + str(subtotal_cost))
print("tax = " + str(tax))
print("total_cost = " + str(total_cost))