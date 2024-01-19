row = int(input())

matrix = []
flat = []

for row_index in range(row):
    row_data = [int(el) for el in input().split(', ')]
    matrix.append(row_data)

for i in matrix:
    for j in i:
        flat.append(j)

print(flat)