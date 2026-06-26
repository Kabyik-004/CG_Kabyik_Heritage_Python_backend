fuel = float(input("Fuel Cost: "))
hotel = float(input("Hotel Cost: "))
food = float(input("Food Cost: "))
other = float(input("Other Cost: "))

total = fuel + hotel + food + other
avg = total / 5

print("\n--- Travel Report ---")
print("Total Expense:", total)
print("Average Per Day:", avg)