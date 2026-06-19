numbers = [10, 25, 40, 15, 35]

largest = second_largest = -999999

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest)