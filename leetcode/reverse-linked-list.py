class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked = None
        while head:
            linked = ListNode(head.val, linked)
            head = head.next
        return linked
