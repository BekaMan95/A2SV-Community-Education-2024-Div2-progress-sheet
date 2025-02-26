# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree: Optional[TreeNode], min_found: int, max_found: int):
            if not tree:
                return True

            if not min_found < tree.val < max_found:
                return False
            
            return (
                dfs(tree.left, min_found, min(max_found, tree.val)) and 
                dfs(tree.right, max(min_found, tree.val), max_found)
            )
        
        return dfs(root, float('-inf'), float('inf'))
