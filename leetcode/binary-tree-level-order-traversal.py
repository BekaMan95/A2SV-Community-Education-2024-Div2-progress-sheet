class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, que = list(), deque()
        que.append(root)
        
        while que:
            level = list()
            for _ in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            
            res.append(level.copy())
        
        return res
