#!/usr/bin/python3
"""Implementation of 2D matric"""


def rotate_2d_matrix(matrix):
    """Turn 2d matrix 90deg"""
    num = len(matrix)
    for i in range(int(num/2)):
        first = i
        last = num - 1 - i
        for j in range(i, last):
            val = num - 1 - j
            temp = matrix[first][j]
            matrix[first][j] = matrix[val][first]
            matrix[val][first] = matrix[last][val]
            matrix[last][val] = matrix[j][last]
            matrix[j][last] = temp
