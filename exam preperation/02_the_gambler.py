INITIAL_AMOUNT = 100
game_board_size = int(input())

board = []

gambler_row = 0
gambler_col = 0

directions = {
    "up":(-1, 0),
    "down":(1, 0),
    "left":(0, -1),
    "right":(0, 1),
}

for i in range(game_board_size):
    rows_data = list(input())
    board.append(rows_data)
    if 'G' in rows_data:
        gambler_row = i
        gambler_col = rows_data.index('G')

command = input()

while command != 'end':
    if command in directions:
        delta_row, delta_col = directions[command]
        new_row = gambler_row + delta_row
        new_col = gambler_col + delta_col

        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]): #if the index is valid
            board[gambler_row][gambler_col] = '-'
            gambler_row = new_row
            gambler_col = new_col
            current_position = board[gambler_row][gambler_col]

            if current_position == 'W':
                INITIAL_AMOUNT += 100
            elif current_position == 'P':
                INITIAL_AMOUNT -= 200
                if INITIAL_AMOUNT <= 0:
                    print("Game over! You lost everything!")
                    break
            elif current_position == 'J':
                INITIAL_AMOUNT += 100000
                print("You win the Jackpot!")
                print(f"End of the game. Total amount: {INITIAL_AMOUNT}$")
                break

            board[gambler_row][gambler_col] = 'G'
        else:
            print("Game over! You lost everything!")
            break

    command = input()
    
else:
    print(f"End of the game. Total amount: {INITIAL_AMOUNT}$")
if INITIAL_AMOUNT > 0:
    for row in board:
        print(''.join(row))
