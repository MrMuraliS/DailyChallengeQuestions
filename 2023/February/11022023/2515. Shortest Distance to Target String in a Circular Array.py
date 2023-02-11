# 2515. Shortest Distance to Target String in a Circular Array

"""
You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

Example 1:
Input: words = ["practice", "makes", "perfect", "coding", "makes"], target = "makes", startIndex = 2
Output: 1
Explanation: You can reach "makes" from startIndex 2 in 1 step.
- Move to words[(2 - 1 + 5) % 5] = "perfect" with 1 step.
- Move to words[(3 + 1) % 5] = "makes" with 1 step.

Example 2:
Input: words = ["practice", "makes", "perfect", "coding", "makes"], target = "makes", startIndex = 1
Output: 3
Explanation: You can reach "makes" from startIndex 1 in 3 steps.
- Move to words[(1 + 1) % 5] = "makes" with 1 step.
- Move to words[(2 + 1) % 5] = "perfect" with 1 step.
- Move to words[(3 + 1) % 5] = "makes" with 1 step.

"""


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        for index in range(len(words)):
            if (
                words[(startIndex + index) % len(words)] == target
                or words[(startIndex - index) % len(words)] == target
            ):
                return index
        return -1
