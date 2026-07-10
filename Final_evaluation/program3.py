# Q3: All Sorting Algorithms


arr = [64, 25, 12, 22, 11, 90, 45, 31]


# Bubble Sort
def bubble_sort(a):
    a = a.copy()
    print("\nBubble Sort")
    n = len(a)

    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        print(f"Pass {i+1}: {a}")
    return a


# Selection Sort
def selection_sort(a):
    a = a.copy()
    print("\nSelection Sort")

    for i in range(len(a)):
        min_idx = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Pass {i+1}: {a}")

    return a


# Insertion Sort
def insertion_sort(a):
    a = a.copy()
    print("\nInsertion Sort")

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
        print(f"Pass {i}: {a}")

    return a


# Merge Sort
def merge_sort(a):
    if len(a) > 1:

        mid = len(a) // 2

        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1

        print(a)

    return a


# Quick Sort
def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]

    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    result = quick_sort(left) + middle + quick_sort(right)
    print(result)
    return result


print("Final Results")
print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))

print("\nMerge Sort")
print(merge_sort(arr.copy()))

print("\nQuick Sort")
print(quick_sort(arr.copy()))

# Complexity
# Bubble: Best O(n), Avg O(n²), Worst O(n²)
# Selection: Best O(n²), Avg O(n²), Worst O(n²)
# Insertion: Best O(n), Avg O(n²), Worst O(n²)
# Merge: Best/Avg/Worst O(n log n)
# Quick: Best/Avg O(n log n), Worst O(n²)