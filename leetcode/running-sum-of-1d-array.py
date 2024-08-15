class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_val, pfx = 0, []
        for num in nums:
            sum_val += num
            pfx.append(sum_val)
        return pfx
