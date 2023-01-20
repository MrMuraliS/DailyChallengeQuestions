# 1653. Minimum Deletions to Make String Balanced

"""
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans, count = 0, 0
        for i in s:
            if i == "b":
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans
