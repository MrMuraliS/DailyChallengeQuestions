# 143. Reorder List

"""
Given the head of a singly linked list, reorder it in-place such that:

    The first node's value is equal to the last node's value, the second node's value is equal to the second-to-last node's value, and so on.
    The first node is equal to the last node in the reordered list.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Initialise slow and fast pointers
        slow = head
        fast = head.next

        # loop until fast and fast.next is not none
        while fast and fast.next:
            # move the pointers
            slow = slow.next
            fast = fast.next.next

        # start from slow pointer, and reverse the nodes
        current_node = slow.next
        slow.next = None
        previous_node = None

        while current_node:
            current_node.next, previous_node, current_node = (
                previous_node,
                current_node,
                current_node.next,
            )

        head2 = previous_node

        # merge both the list together
        head1 = head
        while head1 and head2:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next
