class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = list()
        while head:
            heapq.heappush(heap, -head.val)
            head = head.next
        
        linked = None
        while heap:
            linked = ListNode(-heapq.heappop(heap), linked)

        return linked
