# Q2: Linear Search and Binary Search

# Time Complexity:
# Linear Search -> O(n)
# Binary Search -> O(log n)
# Binary Search requires a sorted array because it repeatedly
# divides the search space into halves.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


unsorted = [45, 12, 78, 34, 89, 10, 56, 23, 90, 67]
sorted_arr = sorted(unsorted)

target = 56

index = linear_search(unsorted, target)
print("Linear Search:")
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not Found")

index = binary_search(sorted_arr, target)
print("\nBinary Search:")
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not Found")