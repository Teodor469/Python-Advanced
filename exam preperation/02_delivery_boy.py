rows, cols = [int(el) for el in input().split()]

matrix = []

directions = {
    "up":(-1, 0),
    "down":(1, 0),
    "left":(0, -1),
    "right":(0, 1),
}

pizza_boy_row = 0
pizza_boy_col = 0
start_position = None

for i in range(rows):
    rows_data = list(input())
    matrix.append(rows_data)
    if 'B' in rows_data:
        pizza_boy_row = i
        pizza_boy_col = rows_data.index('B')
        start_position = (pizza_boy_row, pizza_boy_col)

command = input()

while True:
    if command in directions:
        delta_row, delta_col = directions[command]
        new_row = pizza_boy_row + delta_row
        new_col = pizza_boy_col + delta_col

        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            if matrix[new_row][new_col] == '*':
                # If the new position is '*', the delivery boy stays in the current position
                command = input()
                continue
            if (pizza_boy_row, pizza_boy_col) != start_position and matrix[pizza_boy_row][pizza_boy_col] != 'R':
                matrix[pizza_boy_row][pizza_boy_col] = '.'
            pizza_boy_row = new_row
            pizza_boy_col = new_col
            current_position = matrix[pizza_boy_row][pizza_boy_col]

            if current_position == "P":
                print("Pizza is collected. 10 minutes for delivery.")
                matrix[pizza_boy_row][pizza_boy_col] = 'R'

            if current_position == "A":
                print("Pizza is delivered on time! Next order...")
                matrix[pizza_boy_row][pizza_boy_col] = "P"
                break
        else:
            print('The delivery is late. Order is canceled.')
            matrix[start_position[0]][start_position[1]] = ' '
            break

    command = input()

for row in matrix:
    print(''.join(row))
