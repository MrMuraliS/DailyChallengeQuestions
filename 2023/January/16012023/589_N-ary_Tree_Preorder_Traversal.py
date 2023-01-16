# 589. N-ary Tree Preorder Traversal

"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if root is None:
            return []
        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        return result
