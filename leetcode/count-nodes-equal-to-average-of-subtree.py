class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(tree):
            nonlocal res
            if not tree:
                return [0, 0]
            
            tot_sum, tot_num = 0, 0
            a, b = dfs(tree.left)
            tot_sum += a
            tot_num += b
            tot_sum, tot_num = dfs(tree.right)
            tot_sum += a
            tot_num += b
            tot_num += 1
            tot_sum += tree.val
            if tot_sum // tot_num == tree.val:
                res += 1
            return [tot_sum, tot_num]
        
        res = 0
        dfs(root)
        return res
