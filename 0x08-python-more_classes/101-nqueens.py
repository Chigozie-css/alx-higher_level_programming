#!/usr/bin/python3
"""Solves the N-queens puzzle."""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return [board_deepcopy(row) for row in board]
    return board

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == "Q"]
    return solution


def xout(board, row, col):
    """X out spots on a chessboard."""

    for c in range(col + 1, len(board)):
        board[row][c] = "x"  # X out all forward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"  # X out all backward spots
    for r in range(row + 1, len(board)):
        board[r][col] = "x"  # X out all spots below
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"  # X out all spots above
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"  # X out diagonally down to the right
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"  # X out diagonally up to the right
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"  # X out diagonally down to the left
        c -= 1

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""

    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("Usage: nqueens N")
        sys.exit(1)

    board_size = int(sys.argv[1])
    chessboard = init_board(board_size)
    all_solutions = recursive_solve(chessboard, 0, 0, [])

    for solution in all_solutions:
        print(solution)
