from functools import reduce

invoice_items = [
    {'item_price': 9.99, 'quantity': 35},
    {'item_price': 799.99, 'quantity': 1},
    {'item_price': 4.99, 'quantity': 22},
]

def calculate_item_subtotal(previous_sum, current_item):
    return previous_sum + (current_item['item_price'] * current_item['quantity'])

subtotal = reduce(calculate_item_subtotal, invoice_items, 0.0)
print(f'{subtotal = }')
