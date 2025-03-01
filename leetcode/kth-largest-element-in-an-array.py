class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res, heap = 0, list()
        
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            res = -heapq.heappop(heap)
        
        return res
