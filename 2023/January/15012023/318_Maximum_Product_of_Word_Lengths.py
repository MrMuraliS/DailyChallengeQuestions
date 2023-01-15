# 318. Maximum Product of Word Lengths

"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result = 0

        def findDuplicates(word: set, word2: set):
            for item in word:
                if item in word2:
                    return True
            return False

        for idx in range(len(words) - 1):
            for j in range(idx + 1, len(words)):
                if not findDuplicates(first := words[idx], second := words[j]):
                    summing = len(first) * len(second)
                    if result < summing:
                        result = summing
        return result
