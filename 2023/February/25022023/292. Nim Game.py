# 292. Nim Game

"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Implement a function that can determine whether you can win the game given the number of stones in the heap.

Example 1:

Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.

Example 2:

Input: n = 1
Output: true

Example 3:

Input: n = 2
Output: true

Constraints:

1 <= n <= 231 - 1

"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
