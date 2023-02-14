# 1415. The k-th Lexicographical String of All Happy Strings of Length n

"""
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        nextLetter = {"a": "bc", "b": "ac", "c": "ab"}
        q = collections.deque(["a", "b", "c"])
        while len(q[0]) != n:
            u = q.popleft()
            for v in nextLetter[u[-1]]:
                q.append(u + v)
        return q[k - 1] if len(q) >= k else ""
