def main():
    cost_per_item = 19.99
    quantity = 5
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax

    # YOUR CODE TO CALCULATE THE TOTALS GOES HERE

    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = ${quantity:0.2f}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')


    # YOUR CODE TO PRINT THE TOTALS GOES HERE

if __name__ == "__main__":
    main()