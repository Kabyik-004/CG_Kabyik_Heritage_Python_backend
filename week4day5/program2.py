name = input("Product Name: ")
price = float(input("Price: "))
dis = float(input("Discount %: "))

save = price * dis / 100
final = price - save

print("\n--- Invoice ---")
print("Product:", name)
print("Discount:", save)
print("Final Price:", final)
print("Saved:", save)