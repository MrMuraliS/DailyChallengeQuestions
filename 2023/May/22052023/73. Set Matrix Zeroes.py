# 73. Set Matrix Zeroes

"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

"""

# Solution 1
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first = []
        second = set()

        for idx, outer in enumerate(matrix):
            if 0 in outer:
                first.append(idx)
            for inidx, inner in enumerate(outer):
                if inner == 0:
                    second.add(inidx)

        for i in first:
            matrix[i] = [0] * len(matrix[i])

        for mat in matrix:
            for j in second:
                mat[j] = 0
