class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(tree):
            if not tree:
                return
            
            heapq.heappush(heap, tree.val)
            dfs(tree.left)
            dfs(tree.right)
        
        val, heap = -1, list()
        dfs(root)
        
        for i in range(k):
            val = heapq.heappop(heap)
        return val
