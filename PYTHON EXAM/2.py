n = int(input())

matrix = []
initial_position = None
initial_armor_value = 300
enemy_aircraft = 4

direction_mapper = {
    "up":(-1, 0),
    "down":(1, 0),
    "left":(0, -1),
    "right":(0, 1),
}

for row_index in range(n):
    data = list(input())

    if "J" in data:
        col_index = data.index("J")
        initial_position = (row_index, col_index)
    matrix.append(data)

current_position = initial_position

while True:
    command = input()
    current_row_index, current_col_index = current_position
    row_movement, col_movement = direction_mapper[command]
    new_row = current_row_index + row_movement
    new_col = current_col_index + col_movement

    if 0 <= new_row < n and 0 <= new_col < n:
        symbol = matrix[new_row][new_col]

        if symbol == "-":
            pass

        elif symbol == "E":
            matrix[new_row][new_col] = "-"
            enemy_aircraft -= 1
            if not enemy_aircraft:
                print("Mission accomplished, you neutralized the aerial threat!")
                break
            elif enemy_aircraft:
                initial_armor_value -= 100
                if initial_armor_value == 0:
                    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
                    break
        elif symbol == "R":
            initial_armor_value = 300
            matrix[new_row][new_col] = "-"

        matrix[current_row_index][current_col_index] = '-'
        current_position = (new_row, new_col)

matrix[new_row][new_col] = 'J'

for row in matrix:
    print(''.join(row))

# def move_jetfighter(matrix, direction, position):
#     directions = {
#         'up': (-1, 0),
#         'down': (1, 0),
#         'left': (0, -1),
#         'right': (0, 1)
#     }
#     x, y = position
#     dx, dy = directions[direction]
#     nx, ny = x + dx, y + dy
#     if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
#         return (nx, ny)
#     return position

# def print_matrix(matrix):
#     for row in matrix:
#         print(''.join(row))

# def solve_task():
#     n = int(input())
#     matrix = [list(input()) for _ in range(n)]
#     armor = 300
#     position = [(i, row.index('J')) for i, row in enumerate(matrix) if 'J' in row][0]
#     while True:
#         command = input()
#         matrix[position[0]][position[1]] = '-'
#         position = move_jetfighter(matrix, command, position)
#         if matrix[position[0]][position[1]] == 'E':
#             armor -= 100
#             matrix[position[0]][position[1]] = '-'
#             if armor == 0:
#                 matrix[position[0]][position[1]] = 'J'
#                 print("Mission failed, your jetfighter was shot down! Last coordinates [{}, {}]!".format(*position))
#                 print_matrix(matrix)
#                 return
#         elif matrix[position[0]][position[1]] == 'R':
#             armor = 300
#             matrix[position[0]][position[1]] = '-'
#         matrix[position[0]][position[1]] = 'J'
#         if 'E' not in sum(matrix, []):
#             print("Mission accomplished, you neutralized the aerial threat!")
#             print_matrix(matrix)
#             return
#     print_matrix(matrix)

# # Call the function to start the simulation
# solve_task()
