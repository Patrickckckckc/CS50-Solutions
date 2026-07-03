import random
from .minimax import best_move
from functions import state


EMPTY = "   "
X = "❌"
O = "⭕"

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


class AI:
    @classmethod
    def easy_mode(cls, board):
        # Get all the empty places
        empty_cells = [
            (r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY
        ]

        if not empty_cells:
            return board

        # Select Empty Spaces
        row, column = random.choice(empty_cells)
        board[row][column] = O

        # End that
        return board

    @classmethod
    def normal_mode(cls, board):

        # If AI can win take it, at leat two of them
        for combo in WINNING_COMBOS:
            values = [board[r][c] for r, c in combo]
            if values.count(O) == 2 and values.count(EMPTY) == 1:
                for r, c in combo:
                    if board[r][c] == EMPTY:
                        board[r][c] = O
                        return board

        # If User can win defend it, at least two of them
        for combo in WINNING_COMBOS:
            values = [board[r][c] for r, c in combo]
            if values.count(X) == 2 and values.count(EMPTY) == 1:
                for r, c in combo:
                    if board[r][c] == EMPTY:
                        board[r][c] = O
                        return board
        # Random
        # End
        return cls.easy_mode(board)

    @classmethod
    def impossible_mode(cls, board):

        # If AI can win take it, at leat two of them
        for combo in WINNING_COMBOS:
            values = [board[r][c] for r, c in combo]
            if values.count(O) == 2 and values.count(EMPTY) == 1:
                for r, c in combo:
                    if board[r][c] == EMPTY:
                        board[r][c] = O
                        return board

        # If User can win defend it, at least two of them
        for combo in WINNING_COMBOS:
            values = [board[r][c] for r, c in combo]
            if values.count(X) == 2 and values.count(EMPTY) == 1:
                for r, c in combo:
                    if board[r][c] == EMPTY:
                        board[r][c] = O
                        return board


        if board[1][1] == EMPTY:
            board[1][1] = O
            return board


        # MINIMAX
        moves = best_move(board, O)

         # Defend with sides in specific situation O middle X in the edges
        sides = [(0,1), (1,0), (1,2), (2,1)]
        if board[1][1] == O:
            opponent_corners = [(r,c) for (r,c) in [(0,0),(0,2),(2,0),(2,2)] if board[r][c] == X]
            if len(opponent_corners) == 2:
                sides_moves = [move for move in moves if move in sides]
                if sides_moves:
                    row, col = random.choice(sides_moves)
                    board[row][col] = O
                    return board


         # Select Corners otherwise random Choice
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]

        corner_moves = [move for move in moves if move in corners]

        if corner_moves:
            row, col = random.choice(corner_moves)
        else:
            row, col = random.choice(moves)

        board[row][col] = O
        return board
