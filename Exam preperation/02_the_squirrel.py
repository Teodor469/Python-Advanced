rows = int(input())

matrix = []

hazel_nuts = 0

squirrel_row = 0
squirrel_col = 0

directions = {
    "up":(-1, 0),
    "down":(1, 0),
    "left":(0, -1),
    "right":(0, 1),
}

command = input().split(', ')

for row_index in range(rows):
    data = list(input())

    if "s" in data:
        squirrel_row = row_index
        squirrel_col = data.index("s")
    matrix.append(data)

while command:
    direction = command.pop(0)
    row_movement, col_movement = directions[direction]
    new_row = squirrel_row + row_movement
    new_col = squirrel_col + col_movement
    

    if not (0 <= new_row < rows and 0 <= new_col < len(matrix[0])):
        print("The squirrel is out of the field.")
        break

    symbol = matrix[new_row][new_col]

    if symbol == "h":
        matrix[new_row][new_col] = "*"
        hazel_nuts += 1
        if hazel_nuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    elif symbol == "*":
        pass
    elif symbol == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    elif not command:
        print("There are more hazelnuts to collect.")
        break

    squirrel_row = new_row
    squirrel_col = new_col

print(f"Hazelnuts collected: {hazel_nuts}")