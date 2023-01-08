# 131. Palindrome Partitioning

"""
Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.
"""

"""
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(s):
            # helper function to check if a string is a palindrome
            return s == s[::-1]

        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                if is_palindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]], res)

        res = []
        dfs(s, [], res)
        return res
