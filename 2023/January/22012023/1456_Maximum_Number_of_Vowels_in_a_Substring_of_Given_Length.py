# 1456. Maximum Number of Vowels in a Substring of Given Length

"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_vowels = 0
        current_vowels = 0
        for i, char in enumerate(s):
            if char in vowels:
                current_vowels += 1
            if i >= k and s[i - k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
        return max_vowels
