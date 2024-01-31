row, col = (int(el) for el in input().split(', '))

matrix = []
total_amount = 0

for _ in range(row):
    rows_data = (int(el) for el in input().split(', '))
    total_amount += sum(rows_data)
    matrix.append(rows_data)

print(total_amount)
print(matrix)