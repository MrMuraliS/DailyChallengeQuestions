# 841. Keys and Rooms

"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.


Example 1:
    Input: rooms = [[1],[2],[3],[]]
    Output: true
    Explanation:
    We visit room 0 and pick up key 1.
    We then visit room 1 and pick up key 2.
    We then visit room 2 and pick up key 3.
    We then visit room 3.
    Since we were able to visit every room, we return true.

Example 2:
    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Create a set to store the rooms that we have visited
        visited = set()
        # Create a queue to store the rooms that we have visited
        queue = [0]
        # While the queue is not empty
        while queue:
            # Get the room number
            room = queue.pop(0)
            # If the room number is not in the visited set
            if room not in visited:
                # Add the room number to the visited set
                visited.add(room)
                # Add the keys in the room to the queue
                queue.extend(rooms[room])
        # If the length of the visited set is equal to the length of the rooms list
        if len(visited) == len(rooms):
            # Return True
            return True
        # Otherwise
        else:
            # Return False
            return False
