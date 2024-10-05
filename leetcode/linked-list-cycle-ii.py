class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head and head.next:
            if head.next in visited:
                return head.next
            visited.add(head)
            head = head.next
        return None
