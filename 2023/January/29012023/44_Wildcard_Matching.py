# 44. Wildcard Matching

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(p):  # Reach full pattern
                return i == len(s)

            if i < len(s) and (s[i] == p[j] or p[j] == "?"):  # Match Single character
                return dfs(i + 1, j + 1)

            if p[j] == "*":
                return (
                    dfs(i, j + 1) or i < len(s) and dfs(i + 1, j)
                )  # Match zero or one or more character

            return False

        return dfs(0, 0)
