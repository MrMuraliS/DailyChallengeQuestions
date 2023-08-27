# 637. Average of Levels in Binary Tree

"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input: root = [3,9,20,null,15,7]
    Output: [3.00000,14.50000,11.00000]

Example 2:
    Input: root = [3,9,20,15,7]
    Output: [3.00000,14.50000,11.00000]

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        totals = []
        oldSums = []

        def helper(curr=root, level=0):
            nonlocal ans, totals, oldSums
            if curr:
                if len(ans) > level:
                    total = totals[level] + 1
                    newSum = oldSums[level] + curr.val
                    ans[level] = round(newSum / total, 5)
                    oldSums[level] = newSum
                    totals[level] = total
                else:
                    ans.append(round(curr.val, 5))
                    totals.append(1)
                    oldSums.append(curr.val)
                helper(curr.left, level + 1)
                helper(curr.right, level + 1)
            return

        helper()
        return ans
