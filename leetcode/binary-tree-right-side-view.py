class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res, que = list(), deque()
        que.append(root)
        
        while que:
            last = -200
            for _ in range(len(que)):
                node = que.popleft()
                last = node.val
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            
            res.append(last)
        
        return res
