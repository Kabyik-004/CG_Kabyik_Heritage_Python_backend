rows  = ['A', 'B', 'C', 'D', 'E']
seats = range(1, 9)


print('Available Seats:')
for row in rows:
    row_seats = []
    for seat in seats:
        row_seats.append(f'{row}{seat}')
    print(' '.join(row_seats))
