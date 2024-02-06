#DEFINING THE VARIABLES

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

#START OF LOGIC

for i in range(rows): #REPRESENTS: every row in the matrix  "i"
    rows_data = [el for el in input().split()]
    matrix.append(rows_data)
    if 'B' in rows_data:
        pizza_boy_row = i # is equal to the relative row in which the letter is found
        pizza_boy_col = rows_data.index('B') # finds the index on which the element is on and assigns the col value relatively


command = input()

while True:
    if command in directions:
        delta_row, delta_col = directions[command] #Taking the value from the command and assigning to these variables
        new_row = pizza_boy_row + delta_row
        new_col = pizza_boy_col + delta_col

    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            matrix[gambler_row][gambler_col] = '-'
            gambler_row = new_row
            gambler_col = new_col
            current_position = matrix[gambler_row][gambler_col]

    command = input()