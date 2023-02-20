# 258. Add Digits

"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

Constraints:

    0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?

"""


class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0

    """ Approch 2"""
    # def addDigits(self, num: int) -> int:
    #     if not num: return 0
    #     tar = num
    #     num = str(tar)
    #
    #     while len(num) > 1:
    #         temp = sum(map(int, num))
    #         tar = temp
    #         num = str(temp)
    #
    #     return tar
