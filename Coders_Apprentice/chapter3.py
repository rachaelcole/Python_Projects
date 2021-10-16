# Find the total price of a number of books

cover_price = 24.95
quantity = 60
before_discount = cover_price * quantity
after_discount = round(before_discount - (before_discount * (40/100)), 2)
print(f'Before discount price: ${before_discount}')
print(f'After discount price: ${after_discount}')

shipping = 3 + (0.75 * (quantity-1))
print(f'Shipping costs: ${shipping}')

total = after_discount + shipping
print(f'= ${total}')
