balance = 10000.0

print("=== Smart ATM System ===")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = input("\nEnter your choice (1-4): ")

match choice:
    case "1":
        print(f"\n💰 Your current balance is: ₹{balance:,.2f}")
        
    case "2":
        deposit = float(input("\nEnter deposit amount: ₹"))
        if deposit > 0:
            balance += deposit
            print(f"✅ ₹{deposit:,.2f} deposited successfully.")
            print(f"💰 New Balance: ₹{balance:,.2f}")
        else:
            print("❌ Invalid deposit amount.")
            
    case "3":
        withdraw = float(input("\nEnter withdrawal amount: ₹"))
        if withdraw <= 0:
            print("❌ Invalid withdrawal amount.")
        elif withdraw <= balance:
            balance -= withdraw
            print(f"✅ ₹{withdraw:,.2f} withdrawn successfully.")
            print(f"💰 Remaining Balance: ₹{balance:,.2f}")
        else:
            print("❌ Transaction Denied: Insufficient balance.")
            
    case "4":
        print("\nThank you for using our ATM. Goodbye!")
        
    case _:
        print("\n❌ Invalid choice! Please select a number between 1 and 4.")