table = [[] for _ in range(5)]

key = 12
table[key % 5].append(key)

print(table)