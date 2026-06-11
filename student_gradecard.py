records = [
    ('Alice', 88), ('Bob', None), ('Carol', 92),
    ('Dave', None), ('Eve', 76)
]


print('--- Grade Report ---')
for name, score in records:
    if score is None:
        print(f'{name}: Absent (skipped)')
        continue
    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
    print(f'{name}: {score} ({grade})')
