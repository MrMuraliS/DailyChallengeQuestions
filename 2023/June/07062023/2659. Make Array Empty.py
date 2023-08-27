# 2659. Make Array Empty

"""
You are given an integer array nums containing distinct numbers, and you can perform the following operations until the array is empty:

If the first element has the smallest value, remove it
Otherwise, put the first element at the end of the array.
Return an integer denoting the number of operations it takes to make nums empty.

Example 1:
    Input: nums = [3,4,-1]
    Output: 5
    Explanation:
        1. Remove the first element (3) and then nums = [4,-1]
        2. Remove the first element (4) and then nums = [-1]
        3. Remove the first element (-1) and then nums = []
        4. Put the first element (-1) to the back of the array and then nums = [-1]
        5. Remove the first element (-1) and then nums = []
        It took 5 operations to make nums empty.

Example 2:
    Input: nums = [1,2,3,4,5]
    Output: 3
    Explanation:
        1. Remove the first element (1) and then nums = [2,3,4,5]
        2. Remove the first element (2) and then nums = [3,4,5]
        3. Remove the first element (3) and then nums = [4,5]
        4. Remove the first element (4) and then nums = [5]
        5. Remove the first element (5) and then nums = []
        It took 5 operations to make nums empty.

Example 3:
    Input: nums = [1]
    Output: 1
    Explanation: Remove the first and only element (1) and then nums = [].

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    All the elements of nums are unique.

"""


# Solution 1
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n, res, turn = len(nums), 1, 1
        idx = sorted(range(n), key=lambda x: nums[x])
        for i in range(1, n):
            turn += idx[i] < idx[i - 1]
            res += turn
        return res
