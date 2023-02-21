# 263. Ugly Number

"""
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: n = 8
Output: true
Explanation: 8 = 2 × 2 × 2

"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # Keep dividing dividend by divisor when division is possible
        def keep_dividing_when_divisible(dividend, divisor):
            while dividend % divisor == 0:
                dividend //= divisor
            return dividend

        # Factorize by dividing with permitted factors
        for factor in [2, 3, 5]:
            n = keep_dividing_when_divisible(n, factor)

        # Check if the integer is reduced to 1 or not.
        return n == 1
