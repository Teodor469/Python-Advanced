row = int(input())

matrix = []

for _ in range(row):
    row_data = [int(el) for el in input().split(', ')]
    matrix.append(row_data)

first_diagonal = 0
second_diagonal = 0
for i in range(len(matrix)):
    first_diagonal += matrix[i][i]

for j in range(len(matrix)):
    second_diagonal += matrix[j][-j - 1]

print(f"Primary diagonal: {', '.join(str(matrix[i][i]) for i in range(row))}. Sum: {first_diagonal}")
print(f"Secondary diagonal: {', '.join(str(matrix[j][-j - 1]) for j in range(row))}. Sum: {second_diagonal}")