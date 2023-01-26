# 32. Longest Valid Parentheses

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        answer = 0
        last = -1

        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        answer = max(answer, i - stack[-1])
                    else:
                        answer = max(answer, i - last)
                else:
                    last = i

        return answer
