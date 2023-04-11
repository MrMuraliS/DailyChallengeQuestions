# 45. Jump Game II

"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000

"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] >= n - 1:
            return 1
        maxReach = nums[0]
        steps = nums[0]
        jumps = 1
        for i in range(1, n):
            if i == n - 1:
                return jumps
            maxReach = max(maxReach, i + nums[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = maxReach - i
        return jumps
