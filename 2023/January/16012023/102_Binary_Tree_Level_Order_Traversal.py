# 102. Binary Tree Level Order Traversal

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            result.append([node.val for node in queue])
            queue = [
                child for node in queue for child in (node.left, node.right) if child
            ]
        return result
