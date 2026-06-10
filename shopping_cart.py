amount = float(input("Enter the total shopping amount (₹): "))

if amount > 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10
else:
    discount = 0

final_bill = amount - discount

print(f"\nOriginal Amount: ₹{amount:,.2f}")
print(f"Discount Applied: ₹{discount:,.2f}")
print(f"Final Payable Amount: ₹{final_bill:,.2f}")