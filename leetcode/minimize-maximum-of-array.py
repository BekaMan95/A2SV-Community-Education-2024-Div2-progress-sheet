class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot, res = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            tot += nums[i]
            res = max(res, math.ceil(tot/(i+1)))
        
        return res
