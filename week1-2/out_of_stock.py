products = [
    {'name': 'Laptop', 'stock': 15},
    {'name': 'Mouse', 'stock': 3},
    {'name': 'Keyboard', 'stock': 0},
    {'name': 'Monitor', 'stock': 8},
]


for product in products:
    if product['stock'] == 0:
        print(f"⛔ {product['name']} is OUT OF STOCK — halting shipment!")
        break
    print(f"✅ {product['name']}: {product['stock']} units available")
