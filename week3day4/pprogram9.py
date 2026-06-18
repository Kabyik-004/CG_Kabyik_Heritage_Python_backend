nums = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(nums)-1, -1, -1):
    reversed_list.append(nums[i])

print(reversed_list)