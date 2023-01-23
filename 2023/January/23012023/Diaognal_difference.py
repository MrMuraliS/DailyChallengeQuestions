# Daignol Difference

"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

"""


def diagonalDifference(arr):
    # Write your code here
    first = [item[idx] for idx, item in enumerate(arr)]
    second = [item[idx] for idx, item in enumerate(arr[::-1])]

    return abs(sum(first) - sum(second))
