#!/usr/bin/python3
""" Module implementing N Queens """
import sys

def isMatch(board, row, column, N):
    """Function determines if queens are compatible"""
    for x in range(row):
        if board[x][column] == 1:
            return False

    for x, y in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, N), range(column, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

def utils_queens(board, row, N, sol_list, cur_sol):
    """Check that all cases are placed"""
    if row == N:
        sol_list.append(cur_sol[:])
        return

    for x in range(N):
        if isMatch(board, row, x, N):
            board[row][x] = 1
            cur_sol.append(x)
            utils_queens(board, row + 1, N, sol_list, cur_sol)
            cur_sol.pop()
            board[row][x] = 0

def test(n, x=[], b=[], c=[]):
    if i < n:
def n_queens(N):
    """SOlves the N queens"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    sol_list = []
    cur_sol = []
    board = [[0 for _ in range(N)] for _ in range(N)]
    utils_queens(board, 0, N, sol_list, cur_sol)

    for sol in sol_list:
        temp = [[y, sol[y]] for y in range(N)]
        print(temp)
    print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n_queens(sys.argv[1])
