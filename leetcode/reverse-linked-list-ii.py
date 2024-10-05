class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cache = list()
        while head:
            cache.append(head.val)
            head = head.next
        
        left, right = left - 1, right - 1
        while left < right:
            cache[left], cache[right] = cache[right], cache[left]
            left, right = left + 1, right - 1
        
        linked = None
        while cache:
            linked = ListNode(cache.pop(), linked)

        return linked
