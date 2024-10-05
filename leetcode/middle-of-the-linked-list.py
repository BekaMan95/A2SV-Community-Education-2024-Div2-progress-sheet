class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = list()
        while head:
            values.append(head)
            head = head.next
        return values[len(values) // 2]
