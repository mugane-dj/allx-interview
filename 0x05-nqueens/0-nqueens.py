#!/usr/bin/python3
"""
Solution to the N queens puzzle where N non-attacking queens are placed
on an N*N chessboard
"""
import sys
from typing import List


def cell_is_safe(board: List[List[int]], row: int, col: int) -> bool:
    """
    The cell_is_safe function checks if a cell within the chessboard
    is safe to place a queen on. The checks include the row on the
    left side and both the upper and lower diagonal of the left side

    :param: board - the chessboard
    :param: row - current row
    :param: col - current column
    :return True is cell is safe, otherwise False
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col) -> List[List[int]]:
    """
    The function solve_nqueens iterates over the chessboard and places
    the queens in the safe cells

    :param: board - board of size N*N
    :param: col - current column
    :return: possible solutions on N placing non-attacking queens
    """
    solutions = []

    def place_queen(col):
        if col >= len(board):
            solutions.append([row[:] for row in board])
            return

        for i in range(len(board)):
            if cell_is_safe(board, i, col):
                board[i][col] = 1
                place_queen(col + 1)
                board[i][col] = 0

    place_queen(col)
    return solutions


def main():
    """Entrypoint"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = solve_nqueens(board, 0)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
