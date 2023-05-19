# 29. Divide Two Integers

"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.


Note:

    Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1].
    For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
    Input: dividend = 0, divisor = 1
    Output: 0

Example 4:
    Input: dividend = 1, divisor = 1
    Output: 1

Constraints:
    -231 <= dividend, divisor <= 231 - 1
    divisor != 0

"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Solution 1 - 32 ms
        """
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            return -dividend
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        res = 0
        while dividend >= divisor:
            dividend -= divisor
            res += 1
        if sign == 1:
            return res
        return -res
        """
        # Solution 2 - 12 ms
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            return -dividend
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        res = 0
        while dividend >= divisor:
            tmp = divisor
            i = 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if sign == 1:
            return res
        return -res
