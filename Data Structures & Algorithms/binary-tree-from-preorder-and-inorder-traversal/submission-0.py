# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        
        p = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:p+1], inorder[:p])
        root.right = self.buildTree(preorder[p+1:], inorder[p+1:])

        return root
