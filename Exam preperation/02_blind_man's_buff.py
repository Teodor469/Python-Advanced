n, m = map(int, input().split())

playground = []
player_row = 0
player_col = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

count_touched_opponents = 0
moves_made = 0

for row_index in range(n):
    data = input().split()
    playground.append(data)

    if "B" in data:
        my_position = [row_index, data.index("B")]
        playground[my_position[0]][my_position[1]] = "-"
        player_row, player_col = my_position

direction = input()

while direction != "Finish":
    row_movement, col_movement = directions[direction]
    new_row = player_row + row_movement
    new_col = player_col + col_movement

    if not (0 <= new_row < n and 0 <= new_col < m):
        direction = input()
        continue

    symbol = playground[new_row][new_col]

    if symbol == "O":
        direction = input()
        continue
    elif symbol == "P":
        playground[new_row][new_col] = "-"
        count_touched_opponents += 1
        moves_made += 1
    elif symbol == "-":
        moves_made += 1

    player_row = new_row
    player_col = new_col

    if count_touched_opponents == 3:
        break

    direction = input()

print("Game over!")
print(f"Touched opponents: {count_touched_opponents} Moves made: {moves_made}")
