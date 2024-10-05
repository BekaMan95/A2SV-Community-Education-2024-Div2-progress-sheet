class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low, high = list(), list()
        while head:
            if head.val < x: low.append(head.val)
            else: high.append(head.val)
            head = head.next
        linked, merged = None, low+high
        while merged:
            linked = ListNode(merged.pop(), linked)

        return linked
