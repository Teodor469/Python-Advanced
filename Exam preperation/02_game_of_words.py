def get_initial_position(matrix, size):
    for row in range(size):
        if 'P' in matrix[row]:
            return [row, matrix[row].index('P')]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

string = input()
size = int(input())
matrix = [list(input()) for _ in range(size)]

player_post = get_initial_position(matrix, size)
matrix[player_post[0]][player_post[1]] = "-"

for _ in range(int(input())):
    command = input()
    r, c = player_post[0] + directions[command][0], player_post[1] + directions[command][1]
    if 0 <= r < size and 0 <= c < size:
        # Update player's position only if the new position is inside the field
        position = matrix[r][c]
        matrix[player_post[0]][player_post[1]] = '-'
        if position != '-':
            string += position
        matrix[r][c] = 'P'
        player_post = [r, c]
    else:
        # Remove the last letter from the string if the new position is outside the field
        string = string[:-1]

print(string)
[print(''.join(row)) for row in matrix]
