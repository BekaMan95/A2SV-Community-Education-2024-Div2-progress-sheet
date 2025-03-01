# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(tree: Optional[TreeNode], path: str):
            if not tree:
                return
            
            if path:
                path += '->'
            
            path += str(tree.val)
            
            if not tree.left and not tree.right:
                paths.append(path)
            
            dfs(tree.left, path)
            dfs(tree.right, path)
        
        paths = list()

        dfs(root, '')

        return paths
