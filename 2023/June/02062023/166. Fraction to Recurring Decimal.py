# 166. Fraction to Recurring Decimal

"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:
    Input: numerator = 1, denominator = 2
    Output: "0.5"

Example 2:
    Input: numerator = 2, denominator = 1
    Output: "2"

Example 3:
    Input: numerator = 2, denominator = 3
    Output: "0.(6)"

Example 4:
    Input: numerator = 4, denominator = 333
    Output: "0.(012)"

Example 5:
    Input: numerator = 1, denominator = 5
    Output: "0.2"

Constraints:
    -231 <= numerator, denominator <= 231 - 1
    denominator != 0
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(res)

        res.append(".")
        seen = {}

        while remainder:
            if remainder in seen:
                res.insert(seen[remainder], "(")
                res.append(")")
                break
            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)
