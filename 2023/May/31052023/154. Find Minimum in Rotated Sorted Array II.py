# 154. Find Minimum in Rotated Sorted Array II

"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [1,3,5]
    Output: 1

Example 2:
    Input: nums = [2,2,2,0,1]
    Output: 0

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.

"""

# My solution:
# Runtime: 44 ms, faster than 97.78% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
