#!/usr/bin/python3
"""N-Queens Solver Module"""

import sys


def initialize_board(size):
    """Create an empty chessboard of size N x N."""
    board = []
    [board.append([]) for i in range(size)]
    [row.append(' ') for i in range(size) for row in board]
    return board


def copy_board(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return board


def extract_solution(board):
    """Extract the positions of queens from a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_attacked_positions(board, row, col):
    """Mark all positions attacked by a queen."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
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
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_recursive(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle."""
    if queens == len(board):
        solutions.append(extract_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][c] = "Q"
            mark_attacked_positions(tmp_board, row, c)
            solutions = solve_recursive(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialize_board(int(sys.argv[1]))
    solutions = solve_recursive(board, 0, 0, [])
    for sol in solutions:
        print(sol)
