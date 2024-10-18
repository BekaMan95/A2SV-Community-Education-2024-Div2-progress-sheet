class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        
        nums.sort()
        res, r = nums[-1] - nums[0], -4

        for l in range(4):
            res = min(res, nums[r] - nums[l])
            r += 1
        
        return res
