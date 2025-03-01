# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(order: list):
            if not order:
                return None
            
            tree = TreeNode(order.pop())
            mid = len(order)-1
            
            if order and order[-1] < tree.val:
                while len(order) > mid > -1 and order[mid] < tree.val:
                    mid -= 1
                
                tree.left = dfs(order[mid+1:])
            
            tree.right = dfs(order[:mid+1])
            
            return tree

        preorder.reverse()

        return dfs(preorder)
