# 1716. Calculate Money in Leetcode Bank

"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.



Example 1:
    Input: n = 4
    Output: 10
    Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
    Input: n = 10
    Output: 37

Example 3:
    Input: n = 20
    Output: 96

Constraints:
    1 <= n <= 1000

"""


class Solution:
    N = 7

    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, self.N)
        return (
            weeks * self.N * (self.N + weeks) // 2
            + weeks * days
            + days * (days + 1) // 2
        )
