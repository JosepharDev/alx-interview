#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """

    if n <= 0:
        return list()
    first_row = [1]
    rows = [first_row]

    for _ in range(1, n):
        row = [1]
        for i in range(1, len(rows[-1])):
            num = rows[-1][i-1] + rows[-1][i]
            row.append(num)
        row.append(1)
        rows.append(row)
    return rows
