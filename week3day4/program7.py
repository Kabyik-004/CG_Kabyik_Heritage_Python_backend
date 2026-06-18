nums = [10, 45, 23, 89, 12]

largest = second = float('-inf')

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest =", second)