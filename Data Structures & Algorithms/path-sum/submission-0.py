# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0

        def dfs(root):
            nonlocal sum
            if not root:
                return False
            
            sum += root.val

            if not root.left and not root.right and sum == targetSum:
                return True
            elif not root.left and not root.right and sum != targetSum:
                sum -= root.val
                return False

            if dfs(root.left):
                return True

            if dfs(root.right):
                return True

            sum -= root.val
            return False

        return dfs(root)

            