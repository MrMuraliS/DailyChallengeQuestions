# 2169. Count Operations to Obtain Zero

"""
Given an integer n, return the minimum number of operations needed to obtain the number 0.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or num2 = 0.

Example 1:
    Input: n = 9
    Output: 3
    Explanation: num1 = 9, num2 = 0
    1st operation: subtract 9 from 9, obtain num1 = 0, num2 = 0
    2nd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    3rd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0

Example 2:
    Input: n = 8
    Output: 4
    Explanation: num1 = 8, num2 = 0
    1st operation: subtract 8 from 8, obtain num1 = 0, num2 = 0
    2nd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    3rd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    4th operation: subtract 0 from 0, obtain num1 = 0, num2 = 0

Example 3:
    Input: n = 7
    Output: 5
    Explanation: num1 = 7, num2 = 0
    1st operation: subtract 7 from 7, obtain num1 = 0, num2 = 0
    2nd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    3rd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    4th operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    5th operation: subtract 0 from 0, obtain num1 = 0, num2 = 0

Example 4:
    Input: n = 6
    Output: 4
    Explanation: num1 = 6, num2 = 0
    1st operation: subtract 6 from 6, obtain num1 = 0, num2 = 0
    2nd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    3rd operation: subtract 0 from 0, obtain num1 = 0, num2 = 0
    4th operation: subtract 0 from 0, obtain num1 = 0, num2 = 0

"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt += 1
        return cnt
