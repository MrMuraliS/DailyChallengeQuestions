# 2125. Number of Laser Beams in a Bank

"""
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

Example 1:
Input: bank = ["100","110","111"]
Output: 1
Explanation: The bank has 3 security devices. The laser beams between the first and second security devices are shown in red, and the laser beam between the second and third security devices is shown in green.

Example 2:
Input: bank = ["111","111","111"]
Output: 0
Explanation: There are no laser beams in the bank.

Example 3:
Input: bank = ["101","000","101","000","101"]
Output: 4
Explanation: The bank has 5 security devices. The laser beams between the first and second security devices are shown in red, the laser beams between the second and third security devices are shown in green, and the laser beams between the fourth and fifth security devices are shown in blue.

Constraints:
m == bank.length
n == bank[i].length
1 <= m, n <= 100
bank[i][j] is either '0' or '1'.
There is at least one security device in the bank.

"""


class Solution:
    def numberOfBeams(self, arr: List[str]) -> int:
        li = [-1]
        flag = 0
        summ = 0
        for i in range(len(arr)):
            laser = arr[i].count("1")
            if li[-1] == -1:
                li.append(laser)
            elif li[-1] == 0 and laser == 0:
                li.append(-1)
            elif laser == 0:
                pass
            else:
                summ += li[-1] * laser
                li.append(laser)
        return summ
