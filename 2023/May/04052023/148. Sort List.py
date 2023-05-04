# 148. Sort List

"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

"""

# Solution 1
"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort()

        head = ListNode(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next

        return head


# Solution 2
"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort()

        head = ListNode(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next

        return head
