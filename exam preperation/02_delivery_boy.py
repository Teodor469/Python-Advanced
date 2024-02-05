rows, cols = [int(el) for el in input().split()]

matrix = []

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


for i in range(rows):
    rows_data = [el for el in input().split()]
    matrix.append(rows_data)
    if 'B' in rows_data:
        pass

print(matrix)