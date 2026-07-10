# Q1: BMI Calculator and Age Finder

from datetime import datetime

try:
    # BMI Calculator
    height = float(input("Enter height (in meters): "))
    weight = float(input("Enter weight (in kg): "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"\nBMI = {bmi:.2f}")
    print(f"Category = {category}")

    # Age Finder
    birth_year = int(input("\nEnter your birth year: "))
    current_year = datetime.now().year
    age = current_year - birth_year

    print(f"You are {age} years old.")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
    """Enter height (in meters): 1.3
Enter weight (in kg): 44

BMI = 26.04
Category = Overweight

Enter your birth year: 2004
You are 22 years old."""