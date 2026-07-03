 # TIC TAC TOE
    #### Video Demo:  http://youtube.com/watch?v=38B36ubisLM
    #### Description:

## Project Overview
This project implements a Tic-Tac-Toe game in Python. It supports both two-player mode and a single-player mode against the computer.
In the single-player mode, you can choose the difficulty level: Easy, Normal, or Impossible.

## Helper Functions

### `board_creation`
Creates the Tic-Tac-Toe board as a list with 9 spaces using a loop.
This function also defines three constants used throughout the code:
- **X** → ❌
- **O** → ⭕
- **EMPTY** → `"   "` (three spaces).
The three spaces are chosen because the emojis are visually larger than a single space in the terminal. With two spaces the alignment was better, but three spaces provided the perfect balance.

### `choose_mode`
Allows the user to select one of four game modes:
- Two-player mode
- AI (Easy, Normal, Impossible)

If the input is invalid, the program repeatedly prompts the user with:
`Invalid option. Please type '2 players' or 'AI'.`

### `tabulate` (imported)
The `tabulate` library is used to print the board in a clean, stylish format.

### `full_board`
Checks whether the board is completely filled.
It iterates through each cell, and if no cell contains the `EMPTY` constant, the board is considered full.

### `available_movements`
Validates whether a move is correct.
- Input: a board and a move `(row, col)`
- Ensures that row and column indices are within `0, 1, 2`.
- If the move is invalid, raises a custom `MoveError` with the message `"Invalid Input"`.
- If the chosen cell is already occupied, raises a `MoveError` with the message `"Already Used"`.
- Otherwise, returns the row and column, confirming the move is valid.

### `user_turn`
Handles user input for moves.
- Input: a board, with optional `row` and `col` (default `None`).
- Displays `"Player 1"` for ❌ or `"Player 2"` for ⭕ in two-player mode.
- If `row` or `col` is `None`, prompts the user to enter numbers.
- Invalid input raises a `ValueError`.
- Valid moves are checked using the `available_movements` function.

### `check_winner`
Determines if there is a winner.
- Contains a list of all possible winning combinations.
- Iterates through the board to check if any combination meets the win condition.
- If a winner is found, returns the winning player.
- If the board is full, returns `"Draw"`.
- If no winner and the board is not full, returns `None`.

## AI Easy and Normal Mode
### Class AI
I have created a class call AI that is going to take all of the 3 difficult modes that we have.
Btw the AI is going to have always the turn player: O.
### `AI.easy_mode`
This mode iterates over each cell of the board to find empty spaces.
It collects all available moves into a list, then uses Python’s `random` function to select one move at random.
The board is updated with the chosen move and returned.

### `AI.normal_mode`
The normal mode follows a three-step strategy:
1. **Win if possible** – Iterates over the board and checks against all winning combinations.
   If at least two positions in a combination contain ⭕ and the third is empty, the AI places its move there to win.
2. **Defend if necessary** – Uses the same logic but checks for ❌.
   If the opponent is about to win, the AI blocks by taking the empty spot.
3. **Fallback** – If neither winning nor defending is possible, the AI selects a random empty space, similar to easy mode.

## Minimax

### `actions`
Generates a list of all possible moves.
It iterates over the board and adds each cell that is `EMPTY` to the list of available actions.

### `result`
Defines the new board state after a move.
- Input: a board, an action, and a player.
- Creates a copy of the board (`new_board`) to avoid modifying the original.
- Applies the move to the copy and returns the updated board.

### `minimax`
Implements the minimax algorithm to evaluate board states.
- Returns **-1** if ⭕ wins, **0** for a draw, or **1** if ❌ wins.
- Input: a board and a `maximizing` flag (default `True`).
- First checks if the board is full or if there is a winner, returning the corresponding score.
- If `maximizing` is `True`, the algorithm simulates ❌’s turn, choosing the maximum score among possible moves.
- If `maximizing` is `False`, it simulates ⭕’s turn, choosing the minimum score.
- For each possible action, it recursively calls `minimax` on the resulting board, alternating the `maximizing` flag.

### `best_move`
Determines the best possible move for a given player using minimax.
- Input: a board and a player.
- For ❌, initializes the best value to the lowest possible score and looks for the maximum.
- For ⭕, initializes the best value to the highest possible score and looks for the minimum.
- Iterates through all actions, evaluates each with `minimax`, and collects moves that match the best score.
- If a new best score is found, resets the list to only those moves.
- Returns the list of best moves.

## AI Impossible Mode

### `AI.impossible_mode`
This mode uses a more advanced strategy compared to Easy and Normal:

1. **Win if possible** – Prioritizes completing a winning combination if available.
2. **Defend if necessary** – Blocks the opponent from winning, similar to Normal mode.
3. **Take the center** – If the center cell is empty, the AI chooses it because it provides the strongest advantage.
4. **Special case: corners vs. sides** – If the AI controls the center and the opponent has taken two opposite corners, the best move is to play on a side cell. This prevents an unavoidable loss.
5. **Use minimax for best moves** – Calls the `best_moves` function to evaluate optimal moves using the minimax algorithm.
6. **Corner preference** – If a corner is available among the best moves, the AI selects it.
7. **Fallback** – If no strategic move is found, the AI makes a random choice from the available moves.

This layered approach ensures the AI plays optimally, making it very difficult (or nearly impossible) for the opponent to win.
## Main Function

The `main()` function serves as the entry point of the program.

1. **Initialization**
   - Calls `choose_mode()` to select the game mode.
   - Calls `board_creation()` to create the initial board.
   - Prints the board in a tabulated format along with the game rules.

2. **Choosing the Starting Player**
   - Prompts the user to decide who will start first: ❌ or ⭕.
   - If the input is invalid, the program continues looping until a valid choice is made.

3. **Game Loop**
   - Runs while the board is not full (`while not full_board(board)`).
   - Behavior depends on the selected mode:
     - **Two-player mode** → Uses `user_turn()` for each player’s move.
     - **AI mode** →
       - For ❌ (human turn), calls `user_turn()`.
       - For ⭕ (AI turn), selects the move based on difficulty:
         - Easy → `AI.easy_mode()`
         - Normal → `AI.normal_mode()`
         - Impossible → `AI.impossible_mode()`
       - After each AI move, the turn switches back to ❌ for the human player.

4. **Board Updates and Winner Check**
   - After each move, prints the current board.
   - Calls `check_winner()` to determine if there is a winner.
   - If a winner is found, the loop breaks immediately.

5. **End of Game**
   - Once the loop ends, prints the result returned by `check_winner()` (❌ wins, ⭕ wins, or Draw).
