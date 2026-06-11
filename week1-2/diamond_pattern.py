rows = 5
for i in range(1, rows + 1):
    # Print leading spaces
    for s in range(rows - i):
        print(' ', end='')
    # Print stars
    for j in range(2 * i - 1):
        print('*', end='')
    print()
