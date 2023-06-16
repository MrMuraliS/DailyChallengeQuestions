# 2574. Left and Right Sum Differences

"""
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

Example 1:
    Input: nums = [2,1,3,4,5]
    Output: [1,4,3,4,5]
    Explanation:
        The array answer is equal to abs(leftSum - rightSum) where:
        leftSum = [0,2,3,6,10] where leftSum[0] = 0 because indices are 0-indexed.
        rightSum = [15,13,12,9,5] where rightSum[4] = 0 because indices are 0-indexed.
        abs(leftSum - rightSum) = [15,11,9,3,5].
        answer = [15,11,9,3,5].

Example 2:
    Input: nums = [1,1,1,1,1,1]
    Output: [0,0,0,0,0,0]
    Explanation:
        leftSum = [0,1,2,3,4,5]
        rightSum = [15,14,13,12,11,10]
        abs(leftSum - rightSum) = [15,13,11,9,7,5].
        answer = [15,13,11,9,7,5].

Example 3:
    Input: nums = [2,1,2,1]
    Output: [0,2,0,2]
    Explanation:
        leftSum = [0,2,3,5]
        rightSum = [10,9,7,6]
        abs(leftSum - rightSum) = [10,7,3,1].
        answer = [10,7,3,1].

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 104

"""


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        count = 0
        answer = []
        while count < len(nums):
            leftSum = sum(nums[:count])
            rightSum = sum(nums[count + 1 :])
            answer.append(abs(leftSum - rightSum))
            count += 1
        return answer
