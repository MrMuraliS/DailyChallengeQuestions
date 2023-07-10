# 2428. Maximum Sum of an Hourglass

"""
You are given an m x n integer matrix grid.

We define an hourglass as a part of the matrix with the following form:

Return the maximum sum of the elements of an hourglass.

Note that an hourglass cannot be rotated and must be entirely contained within the matrix.

Example 1:
    Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
    Output: 30
    Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.

Example 2:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
    Output: 35
    Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.

Example 3:
    Input: grid = [[5]]
    Output: 5

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100

"""


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        cur = 0

        for i in range(len(grid) - 2):
            for j in range(1, len(grid[0]) - 1):
                cur = (
                    sum(grid[i][j - 1 : j + 2])
                    + grid[i + 1][j]
                    + sum(grid[i + 2][j - 1 : j + 2])
                )
                res = max(res, cur)

        return res
