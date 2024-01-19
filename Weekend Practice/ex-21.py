row, col = [int(el) for el in input().split(', ')]

matrix = []
flattened = []

for i in range(row):
    values = [int(el) for el in input().split(', ')]
    matrix.append(values)
    
for i in matrix:
    for j in i:
        flattened.append(j)

print(sum(flattened))
print(matrix)