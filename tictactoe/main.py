# Function to display the Tic Tac Toe board
def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))

# Function to check if the board is full
def check_full_board(board):
    return " " not in board

# Function to get player's move
def get_player_move(board, player):
    while True:
        move = input("Player " + player + ", enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            return int(move) - 1
        else:
            print("Invalid move. Please enter a number between 1 and 9.")

# Main function to run the game
def play_game():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Player 1: X, Player 2: O\n")

    while True:
        display_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print("Player " + current_player + " wins!")
            break
        elif check_full_board(board):
            display_board(board)
            print("It's a tie!")
            break
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

# Start the game
play_game()
