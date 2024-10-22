class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res, que = 1, deque()
        que.append((root, 1))
        while que:
            for _ in range(len(que)):
                node, num = que.popleft()

                if node.left:
                    que.append((node.left, num*2))
                if node.right:
                    que.append((node.right, num*2+1))
            
            if que:
                res = max(res, que[-1][1] - que[0][1] + 1)
        
        return res
