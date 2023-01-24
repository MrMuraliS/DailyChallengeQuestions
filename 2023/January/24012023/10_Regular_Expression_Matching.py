# 10. Regular Expression Matching


"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re

        result = re.findall(p, s)
        if result:
            return result[0] == s
        else:
            return False
