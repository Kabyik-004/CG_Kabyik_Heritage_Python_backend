table = [None]*5

key = 12
i = key % 5

while table[i] != None:
    i = (i+1)%5

table[i] = key
print(table)