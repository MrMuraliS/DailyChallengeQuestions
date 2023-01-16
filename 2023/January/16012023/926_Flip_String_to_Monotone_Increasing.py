# 926. Flip String to Monotone Increasing

"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c == "0":
                m += 1
        ans = m
        for c in s:
            if c == "0":
                m -= 1
                ans = min(ans, m)
            else:
                m += 1
        return ans
