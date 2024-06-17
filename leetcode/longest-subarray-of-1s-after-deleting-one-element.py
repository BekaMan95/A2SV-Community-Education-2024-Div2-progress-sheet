class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len, count = 0, defaultdict(int)
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[0] > 1:
                count[nums[l]] -= 1
                l += 1
            if count[0]:
                max_len = max(max_len, count[1])
            else:
                max_len = max(max_len, count[1]-1)
        return max_len
