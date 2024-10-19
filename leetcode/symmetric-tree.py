class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
            nonlocal same
            if not tree1 and not tree2:
                return
            
            if (
                (tree1.left and not tree2.right) or
                (not tree1.left and tree2.right) or
                (tree1.right and not tree2.left) or
                (not tree1.right and tree2.left) or
                (tree1.val != tree2.val)
            ):
                same = False
                return
            
            dfs(tree1.left, tree2.right)
            dfs(tree1.right, tree2.left)
        
        if (root.left and not root.right) or (not root.left and root.right):
            return False
        if not root.left and not root.right:
            return True
        
        same = True
        dfs(root.left, root.right)
        return same
