# 1003. Check If Word Is Valid After Substitutions

"""
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        while "abc" in s:
            s = s.replace("abc", "")
        return s == ""
