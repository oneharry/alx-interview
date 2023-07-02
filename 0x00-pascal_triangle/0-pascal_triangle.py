#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """Implement pascal triangle"""
    outer_list = []
    
    for x in range(n):
        inner_list = []
        for i in range(x + 1):
            if (i == 0 or i == x):
                inner_list.append(1)
            else:
                val = outer_list[x - 1][i - 1] + outer_list[x - 1][i]
                inner_list.append(val)
        outer_list.append(inner_list)
    return outer_list
