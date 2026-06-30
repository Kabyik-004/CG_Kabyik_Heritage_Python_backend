s = input()
seen = set()
ans = ""

for c in s:
    if c not in seen:
        seen.add(c)
        ans += c

print(ans)