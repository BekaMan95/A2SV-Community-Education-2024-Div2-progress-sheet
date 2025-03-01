# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(tree: Optional[TreeNode], prev_sum: int):
            if not tree:
                return 0
            
            res, cur_sum = 0, prev_sum + tree.val
            res += count[cur_sum - targetSum]
            count[cur_sum] += 1
            
            res += dfs(tree.left, cur_sum) + dfs(tree.right, cur_sum)
            count[cur_sum] -= 1

            return res
        
        count = defaultdict(int)
        count[0] += 1

        return dfs(root, 0)
