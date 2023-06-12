# 2733. Neither Minimum nor Maximum

"""
Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.

Example 1:
    Input: nums = [3,2,1,4]
    Output: 2
    Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.

Example 2:
    Input: nums = [1,1,1]
    Output: -1
    Explanation: The minimum value is 1, and the maximum value is 1. Therefore, there is no valid answer.

Constraints:
    1 <= nums.length <= 104
    1 <= nums[i] <= 104
    All the values of nums are unique.

"""


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        nums.sort()
        return nums[1] if nums[1] != min(nums) and nums[1] != max(nums) else -1
