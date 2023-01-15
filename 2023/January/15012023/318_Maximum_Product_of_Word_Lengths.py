# 318. Maximum Product of Word Lengths

"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxProduct = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not set(words[i]) & set(words[j]):
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
        return maxProduct
