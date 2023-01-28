# 43. Multiply Strings

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

Follow up: Could you solve it using only O(n) multiplication algorithm, where n is the number of digits in both num1 and num2?

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        else:
            num1 = num1[::-1]
            num2 = num2[::-1]
            ans = []
            for i in range(len(num1)):
                for j in range(len(num2)):
                    if len(ans) <= i + j:
                        ans.append(0)
                    ans[i + j] += int(num1[i]) * int(num2[j])
            for i in range(len(ans)):
                if ans[i] >= 10:
                    if len(ans) <= i + 1:
                        ans.append(0)
                    ans[i + 1] += ans[i] // 10
                    ans[i] = ans[i] % 10
            ans = ans[::-1]
            ans = [str(i) for i in ans]
            ans = "".join(ans)
            return ans
