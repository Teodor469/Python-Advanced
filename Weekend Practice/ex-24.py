row, col = [int(el) for el in input().split(', ')]

matrix = []

for _ in range(row):
    row_data = [int(i) for i in input().split()]
    matrix.append(row_data)

for col_index in range(col):
    total_col = 0
    for row_index in range(row):
        total_col += matrix[row_index][col_index]
    print(total_col)