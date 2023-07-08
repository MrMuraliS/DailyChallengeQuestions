# 1043. Partition Array for Maximum Sum

"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.


Example 1:
    Input: arr = [1,15,7,9,2,5,10], k = 3
    Output: 84
    Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
    Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
    Output: 83

Example 3:
    Input: arr = [1], k = 1
    Output: 1


Constraints:
    1 <= arr.length <= 500
    0 <= arr[i] <= 109
    1 <= k <= arr.length

"""


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        # handle the first k indexes differently
        for j in range(k):
            dp[j] = max(arr[: j + 1]) * (j + 1)

        # we can get rid of index i by running i times
        for j in range(k, n):
            curr = []
            for m in range(k):
                curr.append(dp[j - m - 1] + max(arr[(j - m) : (j + 1)]) * (m + 1))
            dp[j] = max(curr)

        return dp[-1]
