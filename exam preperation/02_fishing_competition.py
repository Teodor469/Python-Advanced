fishing_area = int(input())

matrix = []

directions = {
    "up":(-1, 0),
    "down":(1, 0),
    "left":(0, -1),
    "right":(0, 1),
}


for _ in range(fishing_area):
    rows_data = [el for el in input().split()]
    matrix.append(rows_data)

