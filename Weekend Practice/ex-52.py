n = int(input())

matrix = []
for _ in range(n):
    row = [int(el) for el in input().split(', ')]
    matrix.append(row)

primary = []
for r in range(n):
    primary.append(matrix[r][r])

second = []
for r in range(n):
    second.append(matrix[r][n - r - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")