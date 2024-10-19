class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(tree: Optional[TreeNode]):
            nonlocal sub
            if not tree:
                return
            if tree.val == val:
                sub = tree
                return
            if tree.val > val:
                dfs(tree.left)
            else:
                dfs(tree.right)
        
        sub = None
        dfs(root)
        return sub
