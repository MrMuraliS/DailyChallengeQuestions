# 160. Intersection of Two Linked Lists

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
begin to intersect at node c1.


Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5],
    Output: Intersected at '8'
    Explanation: The intersected node's value is 8
        (note that this must not be 0 if the two lists intersect).
        From the head of A, it reads as [4,1,8,4,5].
        From the head of B, it reads as [5,6,1,8,4,5].
        There are 2 nodes before the intersected node
        in A; There are 3 nodes before the intersected node in B.


Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4],
    Output: Intersected at '2'
    Explanation: The intersected node's value is 2
        (note that this must not be 0 if the two lists intersect).
        From the head of A, it reads as [1,9,1,2,4].
        From the head of B, it reads as [3,2,4].
        There are 3 nodes before the intersected node in A;
        There are 1 node before the intersected node in B.


Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5],
    Output: No intersection
    Explanation: From the head of A, it reads as [2,6,4].
        From the head of B, it reads as [1,5].
        Since the two lists do not intersect, intersectVal must be 0,
        while pos can be any value.
        Explanation: The two lists do not intersect, so return null.


Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Each value on each linked list is in the range [1, 10^9].
    Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Solution 1
# O(n) time | O(1) space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # get the length of both linked lists
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next

        # move the longer linked list's head forward
        nodeA, nodeB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                nodeA = nodeA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                nodeB = nodeB.next

        # move both linked lists' heads forward until they meet
        while nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next

        return nodeA
