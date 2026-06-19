phonebook = {
    "Alice": "9876543210",
    "Bob": "9123456789",
    "Charlie": "9988776655"
}

name = input("Enter name: ")

if name in phonebook:
    print("Phone:", phonebook[name])
else:
    print("Contact not found")