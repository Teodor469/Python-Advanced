row = int(input())
matrix = []

for row_index in range(row):
    row_data = [int(el) for el in input().split(', ')]
    a = [int(j) for j in row_data if j % 2 == 0]
    matrix.append(a)
print(matrix)