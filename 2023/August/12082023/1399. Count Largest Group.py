# 1399. Count Largest Group

"""
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

Example 1:
    Input: n = 13
    Output: 4
    Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
    [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
    There are 4 groups with largest size.

Example 2:
    Input: n = 2
    Output: 2
    Explanation: There are 2 groups [1], [2] of size 1.


Constraints:
    1 <= n <= 104
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        mapping = {}
        for number in range(1, n + 1):
            sum_of_digits = 0
            while number != 0:
                sum_of_digits += number % 10
                number //= 10
            mapping[sum_of_digits] = mapping.get(sum_of_digits, 0) + 1
        max_val = max(mapping.values())
        ans = list(filter(lambda x: x[1] == max_val, mapping.items()))
        return len(ans)
