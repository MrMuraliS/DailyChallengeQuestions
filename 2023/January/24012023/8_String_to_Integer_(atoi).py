# 8. String to Integer (atoi)

"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1
        res = 0
        for i in range(len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else:
                break
        res = res * sign
        if res < -(2**31):
            return -(2**31)
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
