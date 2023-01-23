# Flipping the matrix

"""
Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer.
He can reverse any of its rows or columns any number of times.
The goal of the game is to maximize the sum of the
elements in the n x n submatrix located in the upper-left corner of the 2n x 2n matrix.
"""


def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    result = 0
    for i in range(n):
        for j in range(n):
            result += max(
                matrix[i][j],
                matrix[i][2 * n - 1 - j],
                matrix[2 * n - 1 - i][j],
                matrix[2 * n - 1 - i][2 * n - 1 - j],
            )
    return result
