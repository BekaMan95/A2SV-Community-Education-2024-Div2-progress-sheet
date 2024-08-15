class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        forward, backward = [], []
        sum_val = 0
        for num in nums:
            sum_val += num
            forward.append(sum_val)
        sum_val = 0
        for num in reversed(nums):
            sum_val += num
            backward.append(sum_val)
        backward.reverse()
        for i in range(len(nums)):
            if forward[i] == backward[i]:
                return i
        return -1
