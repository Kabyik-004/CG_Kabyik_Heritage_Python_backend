numbers = [10, 20, 30, 40, 50]

largest = numbers[0]
smallest = numbers[0]
total = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total += num

average = total / len(numbers)

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Average:", average)