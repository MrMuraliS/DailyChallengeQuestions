# 273. Integer to English Words

"""
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:

0 <= num <= 231 - 1
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        else:

            def dfs(num):
                if num == 0:
                    return ""
                elif num < 20:
                    return [
                        "One",
                        "Two",
                        "Three",
                        "Four",
                        "Five",
                        "Six",
                        "Seven",
                        "Eight",
                        "Nine",
                        "Ten",
                        "Eleven",
                        "Twelve",
                        "Thirteen",
                        "Fourteen",
                        "Fifteen",
                        "Sixteen",
                        "Seventeen",
                        "Eighteen",
                        "Nineteen",
                    ][num - 1] + " "
                elif num < 100:
                    return (
                        [
                            "Twenty",
                            "Thirty",
                            "Forty",
                            "Fifty",
                            "Sixty",
                            "Seventy",
                            "Eighty",
                            "Ninety",
                        ][num // 10 - 2]
                        + " "
                        + dfs(num % 10)
                    )
                elif num < 1000:
                    return dfs(num // 100) + "Hundred " + dfs(num % 100)
                elif num < 1000000:
                    return dfs(num // 1000) + "Thousand " + dfs(num % 1000)
                elif num < 1000000000:
                    return dfs(num // 1000000) + "Million " + dfs(num % 1000000)
                else:
                    return dfs(num // 1000000000) + "Billion " + dfs(num % 1000000000)

            return dfs(num).strip()
