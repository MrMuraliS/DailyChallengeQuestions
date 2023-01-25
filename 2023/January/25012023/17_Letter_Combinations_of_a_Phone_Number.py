# 17. Letter Combinations of a Phone Number

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        for d in digits:
            if not result:
                result = [i for i in num_map[d]]
            else:
                result = [i + j for i in result for j in num_map[d]]
        return result
