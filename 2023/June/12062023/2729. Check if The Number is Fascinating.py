# 2729. Check if The Number is Fascinating

"""
You are given an integer n that consists of exactly 3 digits.

We call the number n fascinating if, after the following modification, the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:

Concatenate n with the numbers 2 * n and 3 * n.
Return true if n is fascinating, or false otherwise.

Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

Example 1:
    Input: n = 192
    Output: false
    Explanation: After concatenating n with 2 * n and 3 * n, we get 192192384.
    This number contains all digits except for the number 0.

Example 2:
    Input: n = 853
    Output: true
    Explanation: After concatenating n with 2 * n and 3 * n, we get 8531706.
    This number contains all digits from 0 to 9 exactly once.

Example 3:
    Input: n = 76
    Output: true

Constraints:
    100 <= n <= 999

"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        number = str(n) + str(2 * n) + str(3 * n)
        return len(set(number)) == len(number) and "0" not in number
