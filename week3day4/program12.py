arr = [1, 2, 2, 2, 3, 4, 5]
x = 2

first = arr.index(x)
last = len(arr) - 1 - arr[::-1].index(x)

print("First:", first)
print("Last :", last)