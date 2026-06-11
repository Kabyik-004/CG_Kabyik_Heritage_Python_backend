balance = float(input("Enter your current account balance: $"))
withdrawal_amount = float(input("Enter the amount you want to withdraw: $"))

print("\nProcessing transaction...")
print("-" * 35)

if withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print(f"✅ Success! You have withdrawn: ${withdrawal_amount:,.2f}")
    print(f"💰 Remaining Balance: ${balance:,.2f}")
else:
    print("❌ Transaction Denied: Insufficient balance.")
    print(f"Your current balance is ${balance:,.2f}, which is less than requested.")