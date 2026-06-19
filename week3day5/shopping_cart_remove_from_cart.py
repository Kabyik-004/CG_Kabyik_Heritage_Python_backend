products = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphone": 2000
}

cart = {}

while True:
    print("\n===== SHOPPING CART MENU =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Calculate Total Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")

        if product in products:
            cart[product] = products[product]
            print(product, "added to cart.")
        else:
            print("Product not available.")

    elif choice == 2:
        product = input("Enter product name to remove: ")

        if product in cart:
            del cart[product]
            print(product, "removed from cart.")
        else:
            print("Product not found in cart.")

    elif choice == 3:
        print("\n--- CART ITEMS ---")
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            for item, price in cart.items():
                print(item, ":", price)

    elif choice == 4:
        total = 0

        print("\n--- FINAL BILL ---")
        for item, price in cart.items():
            print(item, ":", price)
            total += price

        print("Total Bill =", total)

    elif choice == 5:
        print("\n--- FINAL BILL ---")
        total = 0

        for item, price in cart.items():
            print(item, ":", price)
            total += price

        print("Total Bill =", total)
        print("Thank You for Shopping!")
        break

    else:
        print("Invalid Choice!")