students = ['Alice', 'Bob', 'Carol']
subjects = ['Math', 'Science', 'English', 'History']
marks = [
    [88, 92, 76, 81],   # Alice
    [74, 65, 88, 70],   # Bob
    [95, 89, 93, 97],   # Carol
]


print(f'{'Name':<10} {'Total':>6} {'Average':>8}')
print('-' * 28)


for i in range(len(students)):
    total = 0
    for j in range(len(subjects)):    # Inner loop sums marks
        total += marks[i][j]
    avg = total / len(subjects)
    print(f'{students[i]:<10} {total:>6} {avg:>8.1f}')
