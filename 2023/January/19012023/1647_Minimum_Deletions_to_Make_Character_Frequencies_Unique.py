# 1647. Minimum Deletions to Make Character Frequencies Unique

"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

"""


class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter

        counter = list(Counter(s).values())
        counter.sort(reverse=True)

        count = 0
        iteration = 0

        while iteration < len(counter) - 1:
            if counter[iteration] == counter[iteration + 1]:
                count += 1
                if counter[iteration + 1] > 1:
                    counter[iteration + 1] = counter[iteration + 1] - 1
                else:
                    counter.pop(iteration + 1)
                counter.sort(reverse=True)
            else:
                iteration += 1
        print(counter)

        return count
