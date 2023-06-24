# 2716. Minimize String Length

"""
Given a string s, remove all the consecutive duplicates that are present in the given string. That means, if 'aaa' is present in the string then it should become 'a' in the output string.
Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the left of i (if any) and the closest occurrence of c to the right of i (if any).
Your task is to minimize the length of s by performing the above operation any number of times.

Return an integer denoting the length of the minimized string.

Example 1:
    Input: s = "aaabccddd"
    Output: 1
    Explanation:
        Perform the following steps:
        1. Remove 'aaa' -> "abccddd"
        2. Remove 'ccc' -> "abddd"
        3. Remove 'ddd' -> "ab"
        Now there are no consecutive duplicates present in the string.
        Return the length of string after removing all consecutive duplicates, which is 2.

Example 2:
    Input: s = "aaabccd"
    Output: 4
    Explanation:
        Perform the following steps:
        1. Remove 'aaa' -> "abccd"
        2. Remove 'ccc' -> "abd"
        Now there are no consecutive duplicates present in the string.
        Return the length of string after removing all consecutive duplicates, which is 3.


Constraints:
    1 <= s.length <= 105
    s contains only lowercase English letters.

"""

# class Solution:
#     def minString(self, s: str) -> int:
#         stack = []
#         for i in s:
#             if stack and stack[-1] == i:
#                 stack.pop()
#             else:
#                 stack.append(i)
#         return len(stack)


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
