a = [2,7,11,15]
target = 9
d = {}

for i in range(len(a)):
    if target-a[i] in d:
        print(d[target-a[i]], i)
        break
    d[a[i]] = i