# 4. Median of Two Sorted Arrays

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).


Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
    Input: nums1 = [0,0], nums2 = [0,0]
    Output: 0.00000

Example 4:
    Input: nums1 = [], nums2 = [1]
    Output: 1.00000

Example 5:
    Input: nums1 = [2], nums2 = []
    Output: 2.00000


Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6

"""

# Solution 1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = nums1 + nums2
        data.sort()
        n = len(data)

        if n % 2 == 1:
            return data[n // 2]
        else:
            left = data[n // 2 - 1]
            right = data[n // 2]
            return (left + right) / 2
