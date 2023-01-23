# 1081. Smallest Subsequence of Distinct Characters

"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < s.rfind(stack[-1]):
                stack.pop()
            stack.append(c)
        return "".join(stack)
