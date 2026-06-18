nums = [10, 45, 23, 89, 12]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Largest =", largest)