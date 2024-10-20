class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(tree):
            nonlocal lca
            if not tree:
                return
            
            if p.val <= tree.val <= q.val or q.val <= tree.val <= p.val:
                lca = tree
                return
            
            dfs(tree.left)
            dfs(tree.right)
        
        lca = root
        dfs(root)
        return lca
