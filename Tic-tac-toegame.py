def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")

        try:
            row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise ValueError("Invalid input. Please enter numbers between 0 and 2.")
            if board[row][col] != " ":
                raise ValueError("Cell is already occupied. Try again.")

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            turn += 1

        except ValueError as e:
            print(e)
            print("Please try again.")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
