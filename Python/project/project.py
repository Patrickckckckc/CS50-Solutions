from tabulate import tabulate
from functions.game_functions import (
    user_turn,
    full_board,
    board_creation,
    choose_mode,
    check_winner,
)
from functions.ai_functions import AI
from functions import state

# TIC-TAC-TOE GAME
# Globals
EMPTY = "   "
X = "❌"
O = "⭕"


def main():
    mode, board = initialize_game()
    while not full_board(board):
        board = play_turn(board, mode)
        print(tabulate(board, tablefmt="grid"))
        if check_winner(board):
            break
    end_game(board)

def initialize_game():
    # Mode and board setup
    mode = choose_mode()
    board = board_creation()
    print(tabulate(board, tablefmt="grid"))
    print("Select Row: 0-2")
    print("Select Column: 0-2")

    # Who starts?
    while True:
        start_state = input("Who starts? 'X' or 'O': ").strip().upper()
        if start_state == 'X':
            state.turno_x = True
            break
        elif start_state == 'O':
            state.turno_x = False
            break
    return mode, board
def play_turn(board, mode):
    if mode == "2 players":
        board = user_turn(board)
    else:
        if state.turno_x:
            board = user_turn(board)
        else:
            if mode == "easy":
                board = AI.easy_mode(board)
            elif mode == "normal":
                board = AI.normal_mode(board)
            else:
                board = AI.impossible_mode(board)
            state.turno_x = not state.turno_x
    return board

def end_game(board):
    winner = check_winner(board)
    if winner == "Draw":
        print("It´s a Draw")
    else:
        print(f"Winner: {winner}")

if __name__ == "__main__":
    main()

