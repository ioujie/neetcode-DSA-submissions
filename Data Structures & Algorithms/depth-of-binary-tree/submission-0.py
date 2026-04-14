# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def dfs(node, d):
            nonlocal maxD

            if not node:
                return

            d += 1

            dfs(node.left, d)
            dfs(node.right, d)

            maxD = max(d, maxD)

        dfs(root, 0)

        return maxD