# 282. Expression Add Operators

"""
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(l, r, expr, cur, last, res):
            if l == r:
                if cur == target:
                    res.append(expr)
                return
            for i in range(l + 1, r + 1):
                if i == l + 1 or (i > l + 1 and num[l] != "0"):  # prevent "00"
                    s, x = num[l:i], int(num[l:i])
                    if last == None:
                        dfs(i, r, s, x, x, res)
                    else:
                        dfs(i, r, expr + "+" + s, cur + x, x, res)
                        dfs(i, r, expr + "-" + s, cur - x, -x, res)
                        dfs(i, r, expr + "*" + s, cur - last + last * x, last * x, res)

        res = []
        dfs(0, len(num), "", 0, None, res)
        return res
