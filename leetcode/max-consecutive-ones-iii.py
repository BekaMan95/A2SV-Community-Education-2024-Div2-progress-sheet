class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, count = 0, defaultdict(int)
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[0] > k:
                count[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
