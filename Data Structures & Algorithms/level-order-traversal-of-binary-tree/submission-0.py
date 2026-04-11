# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        def bfs(root):
            queue = deque()
            queue.append(root)
            while len(queue) > 0:
                arr = []
                for i in range(len(queue)):
                    cur = queue.popleft()
                    arr.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                ans.append(arr)
        
        bfs(root)

        return ans
                