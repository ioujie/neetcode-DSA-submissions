class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        insNode = TreeNode(key, val)
        
        def dfs(root):
                if not root:
                    return insNode
                
                if root.key < key:
                    root.right = dfs(root.right)
                elif root.key > key:
                    root.left = dfs(root.left)
                else:
                    root.val = insNode.val

                return root

        if self.root == None:
            self.root = insNode
        else:
            dfs(self.root)

            

    def get(self, key: int) -> int:

        def dfs(root):
            if not root:
                return -1

            if root.key < key:
                ans = dfs(root.right)
            elif root.key > key:
                ans = dfs(root.left)
            else:
                ans = root.val

            return ans

        return dfs(self.root)

    def getMin(self) -> int:
        cur = self.root
        if not cur:
            return -1
        while cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        cur = self.root
        if not cur:
            return -1
        while cur.right:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return

        def getMinNode(root):
            cur = root
            while cur.left:
                cur = cur.left
            return cur 

        def dfs(root, key):
            if root.key < key:
                root.right = dfs(root.right, key)
            elif root.key > key:
                root.left = dfs(root.left, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                minNode = getMinNode(root.right)
                root.key, root.val = minNode.key, minNode.val
                root.right = dfs(root.right, minNode.key)

            return root

        self.root = dfs(self.root, key)       
                

    def getInorderKeys(self) -> List[int]:
        arr = []
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            
            arr.append(root.key) 
            
            dfs(root.right)
            
        dfs(self.root)
        return arr    

