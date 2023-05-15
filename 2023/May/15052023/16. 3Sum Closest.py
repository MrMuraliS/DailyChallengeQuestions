# 16. 3Sum Closest

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0

Constraints:
    3 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort the array
        nums.sort()
        # initialize the closest sum
        closest_sum = 0
        # initialize the min difference
        min_diff = float("inf")
        # iterate the array
        for i in range(len(nums)):
            # initialize the left and right pointers
            left = i + 1
            right = len(nums) - 1
            # iterate the array
            while left < right:
                # get the sum
                curr_sum = nums[i] + nums[left] + nums[right]
                # get the difference
                curr_diff = abs(target - curr_sum)
                # check if the difference is less than the min difference
                if curr_diff < min_diff:
                    # update the min difference
                    min_diff = curr_diff
                    # update the closest sum
                    closest_sum = curr_sum
                # check if the sum is less than the target
                if curr_sum < target:
                    # increment the left pointer
                    left += 1
                # check if the sum is greater than the target
                elif curr_sum > target:
                    # decrement the right pointer
                    right -= 1
                # check if the sum is equal to the target
                else:
                    # return the sum
                    return curr_sum
        # return the closest sum
        return closest_sum
