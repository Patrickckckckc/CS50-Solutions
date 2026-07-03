import pytest
from functions.game_functions import (
    full_board,
    user_turn,
    board_creation,
    available_movements,
    check_winner,
    choose_mode,
    MoveError,
)
from functions import state
from unittest.mock import patch
from functions.minimax import actions, result, minimax, best_move
from functions.ai_functions import AI

# CONSTANTS
EMPTY = "   "
X = "❌"
O = "⭕"
turno_x = True


# Board Creation Function
def test_board_creation():
    board = board_creation()
    # Check shape
    assert len(board) == 3
    assert all(len(row) == 3 for row in board)
    # Check all cells are EMPTY
    assert all(cell == EMPTY for row in board for cell in row)


# Full Board Function
def test_full_board():
    # Empty Board
    board = board_creation()
    assert full_board(board) == False
    # Full Board
    for a in range(3):
        for b in range(3):
            board[a][b] = "X"
    assert full_board(board) == True


# Available Movements Function
# INVALID ROW OR COLUMN
def test_invalid_row_col():
    board = board_creation()
    with pytest.raises(MoveError) as exc_info:
        available_movements(board, 5, 1)  # row out of range
    assert str(exc_info.value) == "Invalid Input"
    with pytest.raises(MoveError) as exc_info:
        available_movements(board, 1, -1)  # row out of range
    assert str(exc_info.value) == "Invalid Input"


# SPACED USED
def test_already_used():
    board = board_creation()
    board[0][0] = X
    with pytest.raises(MoveError) as exc_info:
        available_movements(board, 0, 0)  # row out of range
    assert str(exc_info.value) == "Already Used"


# VALID
def test_valid_move_returns_X_then_O():
    board = board_creation()
    state.turno_x = True
    result1 = available_movements(board, 0, 0)
    assert result1 == X
    state.turno_x = False
    result2 = available_movements(board, 1, 1)
    assert result2 == O


# Test Winner
# WINS X
def test_x_wins():
    board = board_creation()
    board[0][2] = board[1][2] = board[2][2] = X
    assert check_winner(board) == X


# WINS O
def test_o_wins():
    board = board_creation()
    board[0][2] = board[1][2] = board[2][2] = O
    assert check_winner(board) == O


# DRAW
def test_draw():
    board = board_creation()
    board[0][2] = board[1][0] = board[1][1] = board[2][1] = X
    board[0][0] = board[0][1] = board[1][2] = board[2][0] = board[2][2] = O
    assert check_winner(board) == "Draw"


# NONE
def test_draw():
    board = board_creation()
    assert check_winner(board) == None


# Two Players Function
def test_two_players_valid():
    board = board_creation()
    state.turno_x = True
    updated = user_turn(board, row=0, column=2)
    state.turno_x = False
    updated = user_turn(board, row=0, column=1)
    assert updated[0][2] == X

    assert updated[0][1] == O


def test_two_players_invalid():
    board = board_creation()
    user_turn(board, row=0, column=-2)
    user_turn(board, row=4, column=1)

    COMPLETE_EMPTY = [
        ["   ", "   ", "   "],
        ["   ", "   ", "   "],
        ["   ", "   ", "   "],
    ]

    assert board == COMPLETE_EMPTY


# Choose Mode
def test_choose_mode_2players():
    with patch("builtins.input", return_value="2 players"):
        assert choose_mode() == "2 players"


def test_choose_mode_ai():
    with patch("builtins.input", side_effect=["ai", "normal"]):
        assert choose_mode() == "normal"
# MINIMAX
# Actions Function
def test_action_available():
    board = board_creation()
    available = actions(board)
    assert available == [(0, 0), (0, 1), (0, 2),
                        (1, 0), (1, 1), (1, 2),
                        (2, 0), (2, 1), (2, 2)]

def test_no_actions():
    board = board_creation()
    for row in (0, 1, 2):
        for col in (0, 1, 2):
            board[row][col] = X
    available = actions(board)
    assert available == []

# Result Function
def test_result():
    board = board_creation()
    action = (1,1)
    player = X
    new_board = result(board, action, player)
    assert new_board[1][1] == player

# Minimax Function
def test_minimax_x_winner():
    board = board_creation()
    # Situation Where X wins
    for r, c in [(0,0), (0,1), (0,2), (1,2), (2,0)]:
        board[r][c] = X

    for r, c in [(1,0), (1,1), (2,1), (2,2)]:
        board[r][c] = O

    assert minimax(board) == 1

def test_minimax_o_winner():
    board = board_creation()
    # Situation Where X wins
    for r, c in [(0,0), (0,1), (0,2), (1,2), (2,0)]:
        board[r][c] = O

    for r, c in [(1,0), (1,1), (2,1), (2,2)]:
        board[r][c] = X

    assert minimax(board) == -1


def test_minimax_draw():
    board = board_creation()
    # Situation Where X wins
    for r, c in [(0,0), (0,1), (1,2), (2,0)]:
        board[r][c] = X

    for r, c in [(0,2), (1,0), (1,1), (2,1), (2,2)]:
        board[r][c] = O

    assert minimax(board) == 0


# best move
def test_best_moves_x():
    board = [
    [X, O, X],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, O, EMPTY]
    ]
    assert [(1,0), (1,1), (1,2), (2,0), (2,2)] == best_move(board, X)


def test_best_moves_o():
    board = [
    [O, X, O],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, X, EMPTY]
    ]
    assert [(1,0), (1,1), (1,2), (2,0), (2,2)] == best_move(board, O)


# AI FUNCTIONS
# Easy Mode
def test_easy_mode():
    board = [
    [O, X, O],
    [X, EMPTY, O],
    [X, X, O]
    ]
    AI.easy_mode(board)
    assert board[1][1] == O

def test_easy_mode_random():
    board = board_creation()
    for _ in range(4):
        AI.easy_mode(board)

    spaces = [(r, c) for r in range(3) for c in range(3) if board[r][c] == O]
    assert len(spaces) == 4


# Normal Mode
def test_normal_mode_winning():
    board = [[O, X, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [O, EMPTY, EMPTY]]
    AI.normal_mode(board)
    assert board[1][0] == O

def test_normal_mode_deffending():
    board = [[X, O, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [X, EMPTY, EMPTY]]
    AI.normal_mode(board)
    assert board[1][0] == O


# Impossible Mode
def test_impossible_mode_empty_board():
    board = board_creation()
    AI.impossible_mode(board)
    assert board[1][1] == O

def test_impossible_mode_deffend_size():
    board = [[X, EMPTY, EMPTY],
             [EMPTY, O, EMPTY],
             [EMPTY, EMPTY, X]]
    board = AI.impossible_mode(board)
    sides = [(r,c) for (r,c) in [(0,1), (1,0), (1,2), (2,1)] if board[r][c] == O]
    assert len(sides) == 1

def test_impossible_mode_corners():
    board = board_creation()
    board[1][1] = X
    AI.impossible_mode(board)
    corners = [(r,c) for (r,c) in [(0,0), (0,2), (2,0), (2,2)] if board[r][c] == O]
    assert len(corners) == 1
