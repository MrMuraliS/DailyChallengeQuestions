# 25. Reverse Nodes in k-Group

"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Example 3:
    Input: head = [1,2,3,4,5], k = 1
    Output: [1,2,3,4,5]

Example 4:
    Input: head = [1], k = 1
    Output: [1]

Constraints:
    The number of nodes in the list is in the range sz.
    1 <= sz <= 5000
    0 <= Node.val <= 1000
    1 <= k <= sz

Follow-up: Can you solve the problem in O(1) extra memory space?

"""

# Solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        modified_values = []
        if len(values) == 1:
            modified_values.extend(values)
        for idx in range(0, len(values) - 1, k):
            temp = values[idx : idx + k]
            if len(temp) >= k:
                temp.reverse()
                modified_values.extend(temp)
            else:
                modified_values.extend(temp)
        if len(values) > 1:
            modified_values.extend(values[idx + k :])
        # print(modified_values)

        target = None
        for item in modified_values:
            if target is None:
                target = ListNode(item)
                temp = target
            else:
                new = ListNode(item)
                temp.next = new
                temp = new

        return target
