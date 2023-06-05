# 179. Largest Number

"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
    Input: nums = [10,2]
    Output: "210"

Example 2:
    Input: nums = [3,30,34,5,9]
    Output: "9534330"

Example 3:
    Input: nums = [1]
    Output: "1"

Example 4:
    Input: nums = [10]
    Output: "10"

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 109

"""


class LargerNumKey(str):
    def __lt__(x, y):
        # Compare x+y with y+x in reverse order to get descending order
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert the list of numbers to list of strings
        nums = [str(num) for num in nums]

        # Sort the list of strings using our custom sorting function
        nums.sort(key=LargerNumKey)

        # Join the sorted list of strings to form the final result
        largest_num = "".join(nums)

        # If the largest number is 0, return "0"
        # Otherwise, return the largest number
        return "0" if largest_num[0] == "0" else largest_num
