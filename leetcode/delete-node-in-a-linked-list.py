class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
