class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx, evens, odds = 0, list(), list()
        
        while head:
            if idx % 2: odds.append(head.val)
            else: evens.append(head.val)
            head = head.next
            idx += 1
        
        linked, merged = None, evens+odds

        while merged:
            linked = ListNode(merged.pop(), linked)

        return linked
