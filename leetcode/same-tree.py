class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
            nonlocal same
            if not tree1 and not tree2:
                return
            
            if (
                (tree1.left and not tree2.left) or
                (not tree1.left and tree2.left) or
                (tree1.right and not tree2.right) or
                (not tree1.right and tree2.right) or
                (tree1.val != tree2.val)
            ):
                same = False
                return
            
            dfs(tree1.left, tree2.left)
            dfs(tree1.right, tree2.right)
        
        if (p and not q) or (not p and q):
            return False
        
        same = True
        dfs(p, q)
        return same
