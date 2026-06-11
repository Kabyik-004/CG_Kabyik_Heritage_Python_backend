cart = {
    'Electronics': [('Laptop', 60000), ('Headphones', 3000)],
    'Clothing':    [('Shirt', 800), ('Jeans', 1500)],
    'Groceries':   [('Rice 5kg', 350), ('Oil 1L', 200)],
}
discounts = {'Electronics': 10, 'Clothing': 20, 'Groceries': 5}


grand_total = 0
for category, items in cart.items():          # Outer loop: category
    print(f'\n--- {category} ({discounts[category]}% off) ---')
    for item, price in items:                 # Inner loop: items
        disc  = price * discounts[category] / 100
        final = price - disc
        grand_total += final
        print(f'  {item:<15} ₹{price:>6,} → ₹{final:>6,.0f}')


print(f'\n{'='*35}')
print(f'Grand Total: ₹{grand_total:,.0f}')
