class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(tree):
            if not tree:
                return
            count[tree.val] += 1
            dfs(tree.left)
            dfs(tree.right)
        
        count = defaultdict(int)
        dfs(root)
        mode_val = max(count.values())
        return [num for num, freq in count.items() if freq == mode_val]
