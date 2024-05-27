class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res, prevOp = 0, 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res += prevOp
            else:
                prevOp += 1
                res += prevOp
        return res
