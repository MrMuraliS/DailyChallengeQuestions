# 12. Integer to Roman

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        class Solution:
            def intToRoman(self, num: int) -> str:
                num_map = {
                    1: "I",
                    5: "V",
                    4: "IV",
                    10: "X",
                    9: "IX",
                    50: "L",
                    40: "XL",
                    100: "C",
                    90: "XC",
                    500: "D",
                    400: "CD",
                    1000: "M",
                    900: "CM",
                }

                # Result Variable
                r = ""

                for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
                    # If n in list then add the roman value to result variable
                    while n <= num:
                        r += num_map[n]
                        num -= n
                return r
