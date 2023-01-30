# 65. Valid Number

"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Example 4:

Input: s = ".1"
Output: true

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

"""

# class Solution:
#     def isNumber(self, s: str) -> bool:
#         @lru_cache(None)
#         def dfs(i):
#             if i == len(s):
#                 return True
#             if s[i] in "0123456789":
#                 return dfs(i + 1)
#             if s[i] == ".":
#                 return dfs(i + 1) or dfs(i + 1) and i + 1 < len(s) and s[i + 1] in "0123456789"
#             if s[i] in "eE":
#                 return dfs(i + 1) and i + 1 < len(s) and s[i + 1] in "+-" and dfs(i + 2) or dfs(i + 1)
#             return False
#         return dfs(0)


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ["+", "-"]:
                if i > 0 and s[i - 1] not in ["e", "E"]:
                    return False
            elif char == ".":
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char in ["e", "E"]:
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit
