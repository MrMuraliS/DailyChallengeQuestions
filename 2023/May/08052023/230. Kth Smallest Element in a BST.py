# 230. Kth Smallest Element in a BST

"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

"""

# Solution 1


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        return inorder(root)[k - 1]


# Solution 2


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            inorder(root.right)

        self.k = k
        inorder(root)
        return self.res


# Solution 3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def extract_values(root):
            values = []

            def dfs(node):
                if node:
                    dfs(node.left)
                    values.append(node.val)
                    dfs(node.right)

            dfs(root)

            return values

        output = extract_values(root)

        output.sort()
        # print(output)
        return output[k - 1]
