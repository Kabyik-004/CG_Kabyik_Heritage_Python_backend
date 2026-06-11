experience = float(input("Enter years of experience: "))
rating = float(input("Enter performance rating (1-5): "))

if experience > 5 and rating >= 4:
    print("\n✅ Eligible for Bonus!")
else:
    print("\n❌ Not Eligible for Bonus.")