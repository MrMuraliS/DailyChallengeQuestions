# 2586. Count the Number of Vowel Strings in Range

"""
You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

Example 1:
Input: words = ["are","amy","u"], left = 0, right = 2
Output: 2
Explanation:
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
The number of vowel strings in the mentioned range is 2.

Example 2:
Input: words = ["a","b","c"], left = 1, right = 2
Output: 0
Explanation:
The number of vowel strings in the mentioned range is 0.

Example 3:
Input: words = ["a","e","i","o","u"], left = 0, right = 4
Output: 15
Explanation:
The number of vowel strings in the mentioned range is 15.

Constraints:
1 <= words.length <= 10^5
1 <= words[i].length <= 10^5
words[i] consists of lowercase English letters.
0 <= left <= right < words.length

"""


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for idx in range(left, right + 1):
            temp = words[idx]
            if temp[0] in set("aeiou") and temp[-1] in set("aeiou"):
                count += 1
        return count
