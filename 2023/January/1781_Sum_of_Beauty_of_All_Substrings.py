# 1781. Sum of Beauty of All Substrings

"""
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.
"""

"""
Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
"""


class Solution:
    def beautySum(self, s: str) -> int:
        def find_diff(val: str):
            from collections import Counter

            counter = Counter(val)
            return max(counter.values()) - min(counter.values())

        total = 0
        for idx in range(len(s) - 1):
            for j in range(idx + 1, len(s) + 1):
                total += find_diff(s[idx:j])
        return total
