# 2235. Add Two Integers

"""
Given two integers num1 and num2, return the sum of the two integers.

Example 1:
    Input: num1 = 12, num2 = 5
    Output: 17
    Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

Example 2:
    Input: num1 = 0, num2 = 100
    Output: 100
    Explanation: num1 is 0, num2 is 100, and their sum is 0 + 100 = 100, so 100 is returned.

Example 3:
    Input: num1 = -14, num2 = 5
    Output: -9
    Explanation: num1 is -14, num2 is 5, and their sum is -14 + 5 = -9, so -9 is returned.

Constraints:
    -10^9 <= num1, num2 <= 10^9

"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
