# Console Tic-Tac-Toe

A simple two-player Tic-Tac-Toe game implemented in Python for the terminal.

## Features

- Two human players choose `X` or `O`.
- Players select positions from 1 to 9.
- The program prevents selecting an occupied or out-of-range position.
- Checks rows, columns, and diagonals for a winner.
- Detects a draw and offers to restart the game.

## Run

```bash
python tic_tac_toe.py
```

## Platform note

The current source uses the Windows `cls` command to clear the terminal. On macOS or Linux, that screen-clearing behavior may not work without a small platform-specific adjustment; the game logic itself uses Python's standard library.

## Requirements

Python 3 only. No third-party packages are required.

## License

No license has been specified.
