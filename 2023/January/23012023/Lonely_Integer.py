# Lonely Integer

"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Example

The unique element is .
"""


def lonelyinteger(a):
    # Write your code here
    from collections import Counter

    counter = list(Counter(a).items())
    counter.sort(key=lambda x: x[1])
    return counter[0][0]
