def is_valid(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

def add(matrix, row, col, num):
    if is_valid(matrix, row, col):
        matrix[row][col] += num
    else:
        print("Invalid coordinates")

def subtract(matrix, row, col, num):
    if is_valid(matrix, row, col):
        matrix[row][col] -= num
    else:
        print("Invalid coordinates")

n = int(input())
matrix = []

for _ in range(n):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

command = input()

while command != 'END':
    command_tokens = command.split()

    if command_tokens[0] == 'Add':
        row = int(command_tokens[1])
        col = int(command_tokens[2])
        num = int(command_tokens[3])
        add(matrix, row, col, num)
    elif command_tokens[0] == 'Subtract':
        row = int(command_tokens[1])
        col = int(command_tokens[2])
        num = int(command_tokens[3])
        subtract(matrix, row, col, num)
    
    command = input()

for row in matrix:
    print(" ".join(map(str, row)))