PLAYER_X = "X"
PLAYER_O = "O"

board = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "
]

current_player= PLAYER_X

def display_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])

        if i < 6:
            print("---------")

def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        a, b, c = combination

        if board[a] == board[b] == board[c] and board[a] in [PLAYER_X,PLAYER_O]:
            return True

    return False

def check_draw():
    for cell in board:
        if cell == " ":
            return False
    return True

def switch_player():
    global current_player
    if current_player == PLAYER_O:
        current_player = PLAYER_X
    else:
        current_player = PLAYER_O

def reset_board():
    global board

    board = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " "
    ]

def play_game():
    global current_player

    current_player = PLAYER_X

    while True:

        display_board()
        print(f"\nPlayer {current_player}'s Turn")

        while True:
            try:
                position = int(
                    input(f"Player {current_player}, enter a position (1-9): ")
                )
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("Cell already occupied. Choose another position.")
                continue

            break

        board[index] = current_player

        if check_winner():
            display_board()
            print(f"\nPlayer {current_player} wins!")
            break

        if check_draw():
            display_board()
            print("\nIt's a draw!")
            break

        switch_player()

def main():

    print("=" * 35)
    print("          TIC TAC TOE")
    print("=" * 35)

    print("\nPlayer 1: X")
    print("Player 2: O")

    while True:

        play_game()

        while True:

            choice = input("\nDo you want to play again? (Y/N): ").upper()

            if choice == "Y":
                reset_board()
                break

            elif choice == "N":
                print("\nThanks for playing Tic Tac Toe!")
                return

            else:
                print("Invalid input! Please enter Y or N.")


if __name__ == "__main__":
    main()

        

