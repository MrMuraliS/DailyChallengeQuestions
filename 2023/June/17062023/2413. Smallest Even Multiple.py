# 2413. Smallest Even Multiple

"""
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

Example 1:
    Input: n = 5
    Output: 10
    Explanation: The smallest multiple of both 5 and 2 is 10.

Example 2:
    Input: n = 1
    Output: 2
    Explanation: The smallest multiple of both 1 and 2 is 2.

Example 3:
    Input: n = 6
    Output: 6
    Explanation: The smallest multiple of both 6 and 2 is 6.

Constraints:
    1 <= n <= 10^5

"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        count = n
        while True:
            if count % 2 == 0 and count % n == 0:
                return count
            count += 1
