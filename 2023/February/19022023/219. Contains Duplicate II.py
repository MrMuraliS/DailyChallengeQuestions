# 219. Contains Duplicate II

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = {}
        for i in range(len(nums)):
            if nums[i] not in l:
                l[nums[i]] = i
            else:
                if i - l[nums[i]] <= k:
                    return True
                else:
                    l[nums[i]] = i
        return False
