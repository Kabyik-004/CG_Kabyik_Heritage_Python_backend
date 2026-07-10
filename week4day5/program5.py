name = input("Student Name: ")
course = input("Course Name: ")
fee = float(input("Course Fee: "))
reg = float(input("Registration Fee: "))

total = fee + reg
advance = total * 0.30
remain = total - advance

print("\n--- Enrollment Summary ---")
print("Name:", name)
print("Course:", course)
print("Total:", total)
print("Advance:", advance)
print("Remaining:", remain)