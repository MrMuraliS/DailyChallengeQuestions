# 147. Insertion Sort List

"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Constraints:
    The number of nodes in the list is in the range [1, 5000].
    -5000 <= Node.val <= 5000

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Initialize the sorted portion of the list to be the first node
        sorted_head = ListNode(0)
        sorted_head.next = head
        sorted_tail = head

        # Start with the second node in the list, since the first node is already sorted
        curr = head.next

        while curr:
            # If the current node is greater than the tail of the sorted list,
            # it is already in the correct place, so just move on to the next node
            if curr.val >= sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
            else:
                # Remove the current node from the list
                sorted_tail.next = curr.next

                # Find the correct position to insert the current node in the sorted list
                insert_pos = sorted_head
                while insert_pos.next.val < curr.val:
                    insert_pos = insert_pos.next

                # Insert the current node into the sorted list
                curr.next = insert_pos.next
                insert_pos.next = curr

                # Move on to the next node in the unsorted portion of the list
                curr = sorted_tail.next

        return sorted_head.next
