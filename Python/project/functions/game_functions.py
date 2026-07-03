from functions import state

# CONSTANTS
EMPTY = "   "
X = "❌"
O = "⭕"


# Globals
class MoveError(Exception):
    pass


# CHOSSES THE GAME MODE
def choose_mode():
    while True:
        game_mode = (
            input("What mode do you wanna play? (2 players / AI): ").strip().lower()
        )
        if game_mode == "2 players":
            return game_mode
        elif game_mode == "ai":
            while True:
                difficult = input("SELECT: Easy - Normal - Impossible: ").lower()
                if difficult in ("easy", "normal", "impossible"):
                    return difficult
        else:
            print("Invalid option. Please type '2 players' or 'AI'.")


# CREATES A BOARD
def board_creation():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    # Board
    return board


# CHECKS IF THE BOARD IS FULL OR NOT
def full_board(board):
    for a in range(3):
        for b in range(3):
            if board[a][b] == EMPTY:
                return False
    return True


# CHECKS IF THE MOVEMENT IS AVAILABLE
def available_movements(board, row, col):
    if row not in (0, 1, 2) or col not in (0, 1, 2):
        print("Invalid Input")
        raise MoveError("Invalid Input")
    # You cannot change already used values
    if board[row][col] != EMPTY:
        print("Already Used")
        raise MoveError("Already Used")

    # Change the value per Play
    else:
        jugador = X if state.turno_x else O
        return jugador


def check_winner(board):

    WINNING_COMBOS = [
        [(0, 0), (0, 1), (0, 2)],  # rows
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],  # cols
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  # diagonals
        [(0, 2), (1, 1), (2, 0)],
    ]

    # Winner X or O
    for combo in WINNING_COMBOS:
        values = [board[r][c] for r, c in combo]
        if values[0] != EMPTY and values.count(values[0]) == 3:
            return values[0]

    # None -> not winner yet
    # Draw -> If Full_board and not winner
    if full_board(board):
        return f"Draw"
    else:
        return None


def user_turn(board, row=None, column=None):
    if state.turno_x == True:
        print("Player 1")
    else:
        print("Player 2")
    if row is None:
        try:
            row = int(input("Row: "))
        except ValueError:
            print("Just numbers")
            return board
    if column is None:
        try:
            column = int(input("Column: "))
        except ValueError:
            print("Just numbers")
            return board
    try:
        board[row][column] = available_movements(board, row, column)
        state.turno_x = not state.turno_x
        return board
    except MoveError:
        print("Invalid Movement")
        return board

