# Tic Tac Toe Game

This project is a graphical Tic Tac Toe game built using Python and the `customtkinter` library. It allows a single player to play against the computer, with simple and intuitive gameplay. The game also detects winning conditions, ties, and includes a restart functionality.

---

## Features
- **Graphical User Interface (GUI):** Interactive grid-based game board.
- **Player vs Computer:** Take turns making moves with a simple AI for the computer.
- **Winning Detection:** Recognizes when a player or the computer wins.
- **Tie Detection:** Declares a tie if no more moves are possible.
- **Restart Game:** Reset the board and start a new game with a single click.

---

## Prerequisites

Ensure you have the following installed:
- Python 3.7+
- `customtkinter` library (for enhanced Tkinter GUI)

Install the required library using pip:
```bash
pip install customtkinter
```

---

## How to Run

1. Clone or download the repository.
2. Save the script as `tictactoe.py`.
3. Open a terminal or command prompt.
4. Run the script:
   ```bash
   python tictactoe.py
   ```
5. Enjoy the game!

---

## Game Rules

1. The player always starts first and uses `X`.
2. The computer uses `O`.
3. Click on any empty cell to make your move.
4. The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins.
5. If all cells are filled without a winner, the game declares a tie.
6. Click the **RESTART** button to reset the game.

---

## Code Overview

- **Winning Combinations:** Defined in the `WINNING_COMBINATION` constant as sets of board positions.
- **Player Moves:** Tracked using `self.user` and `self.computer` sets.
- **Logic:** The `logic` method handles the player’s move, computer’s move, and checks for winning or tie conditions.
- **Restart Functionality:** The `restart_game` method resets the game state for a new round.
- **GUI:** Built using `customtkinter` with buttons for each cell, styled for a modern appearance.

---

## Screenshots

### Initial Game Board:
A 3x3 grid with buttons representing the cells.

### Gameplay:
Player makes moves using `X`, and the computer responds with `O`.

### Winning/Tie Screen:
A pop-up window displays the result (e.g., "YOU WIN", "COMPUTER WINS", or "IT'S A TIE").

---

## Future Improvements

- Add a difficulty selector for the computer AI.
- Support for two-player mode.
- Visual enhancements with animations or themes.
- Sound effects for a better user experience.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Contributions

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.

