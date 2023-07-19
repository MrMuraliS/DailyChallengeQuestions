# 1184. Distance Between Bus Stops

"""
There is a bus circular route with n stops. The distance between adjacent
stops is dist.
We have a list of distance where dist[i] is the distance between the ith
and (i+1)th stops.
Return the minimum distance between any two stops.

Example 1:
    Input: dist = [1,2,3,4], start = 0, destination = 1
    Output: 1
    Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
    Input: dist = [1,2,3,4], start = 0, destination = 2
    Output: 3
    Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:
    Input: dist = [1,2,3,4], start = 0, destination = 3
    Output: 4
    Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

Constraints:
    1 <= n <= 10^4
    dist.length == n
    0 <= start, destination < n
    0 <= dist[i] <= 10^4

"""


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        if start > destination:
            distances = sum(distance[destination:start]), sum(distance[start:]) + sum(
                distance[:destination]
            )
        else:
            distances = sum(distance[start:destination]), sum(
                distance[destination:]
            ) + sum(distance[:start])
        return min(distances)
