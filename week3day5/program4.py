employees = {
    "Alice": 50000,
    "Bob": 60000,
    "Charlie": 55000
}

# Search Employee
name = input("Enter employee name to search: ")

if name in employees:
    print("Salary:", employees[name])
else:
    print("Employee not found")

# Update Salary
employees["Bob"] = 65000
print("Updated Dictionary:", employees)

# Delete Employee
del employees["Charlie"]
print("After Deletion:", employees)