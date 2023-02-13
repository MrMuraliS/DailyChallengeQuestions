# 1529. Minimum Suffix Flips

"""
You are given a binary string nums. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the last character of the string nums and append it to the beginning of the string.
Type-2: Pick a non-empty prefix of nums and flip every character in that prefix. A flip operation changes a 0 to a 1 and a 1 to a 0.

Return the minimum number of type-2 operations you need to perform such that nums becomes alternating.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Example 1:

Input: nums = "111000"
Output: 2
Explanation: Use the first operation two times to make nums = "100011".

Then, use the second operation on the prefix "1", so nums = "110011".

After the second operation, nums = "101010", which is alternating.

Example 2:

Input: nums = "010"
Output: 0
Explanation: nums is already alternating.

Example 3:

Input: nums = "1110"
Output: 1
Explanation: Use the second operation on the prefix "1110" to make nums = "1010".

Constraints:

1 <= nums.length <= 105
nums[i] is either '0' or '1'.

"""


class Solution:
    def minFlips(self, target: str) -> int:
        ans, prev = 0, "0"
        for c in target:
            if prev != c:
                ans += 1
            prev = c
        return ans
