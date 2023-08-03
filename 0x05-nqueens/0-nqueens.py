#!/usr/bin/python3
""" Module implementing N Queens """
import sys

def print_queens(sol):
    print(sol)

def isMatch(board, row, column):
    """Function determines if queens are compatible"""
    for x in range(row):
        if board[x][column] == 1:
            return False

    for x, y in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, len(board)), range(column, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

def utils_queens(board, column, N, sol_list):
    """Check that all cases are placed"""
    if column >= N:
        sol = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    sol.append([i, j])
        sol_list.append(sol)
        return

    for x in range(N):
        if isMatch(board, x, column):
            board[x][column] = 1
            utils_queens(board, column + 1, N, sol_list)
            board[x][column] = 0

def n_queens(N):
    """Solves the N queens"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    sol_list = []
    utils_queens(board, 0, N, sol_list)

    for i, sol in enumerate(sol_list):
        if i >= 2:  # Prints only the first two solutions
            break
        print_queens(sol)
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n_queens(4)