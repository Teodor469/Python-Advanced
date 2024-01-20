rows = int(input())

matrix = []

for _ in range(rows):
    rows_data = [int(el) for el in input().split()]
    matrix.append(rows_data)

diagonal = 0
for i in range(len(matrix)):
    diagonal += matrix[i][i]

# diagonal = [matrix[i][i] for i in range(len(matrix))]
print(diagonal)