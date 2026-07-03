from functions.game_functions import full_board, board_creation, check_winner

EMPTY = "   "
X = "❌"
O = "⭕"

# 1 -> X wins
# 0 -> Tie
# -1 -> O wins

# Result (action, state) -> what is going to happen after

# MINIMAX ALGORYTHMUS
board = board_creation()


def best_move(board, player):
    if player == X:
        best_score = float("-inf")
        best_moves = []
        for action in actions(board):
            score = minimax(result(board, action, player), maximizing=True)
            if score > best_score:
                best_score = score
                best_moves = [action]
            elif score == best_score:
                best_moves.append(action)
        return best_moves
    else:
        best_score = float("inf")
        best_moves = []
        for action in actions(board):
            score = minimax(result(board, action, player), maximizing=False)
            if score < best_score:
                best_score = score
                best_moves = [action]
            elif score == best_score:
                best_moves.append(action)
        return best_moves


# MINIMAX ALGORYTHMUS
def minimax(board, maximizing=True):
    # Check Terminal_State
    if full_board(board):
        winner = check_winner(board)
        if winner == X:
            return 1
        elif winner == O:
            return -1
        else:
            return 0

    # Turn X (MAX)
    if maximizing:
        value = float("-inf")
        for action in actions(board):
            value = max(value, minimax(result(board, action, X), False))
        return value

    # Turn O (MIN)
    else:
        value = float("inf")
        for action in actions(board):
            value = min(value, minimax(result(board, action, O), True))
        return value


# Actions algorythmus
def actions(board):
    available = []
    for row in (0, 1, 2):
        for col in (0, 1, 2):
            if board[row][col] == EMPTY:
                available.append((row, col))
    return available


# Result Algorythmus
def result(board, action, player):
    row, col = action
    new_board = [r[:] for r in board]
    new_board[row][col] = player
    return new_board


