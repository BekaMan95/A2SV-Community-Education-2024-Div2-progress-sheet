class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left_min, right_max = [0]*len(nums), [0]*len(nums)
        val = (2**31)-1
        for i in range(len(nums)):
            val = min(val, nums[i])
            left_min[i] = val
        
        val = -(2**31)-1
        for i in range(len(nums)-1, -1, -1):
            val = max(val, nums[i])
            right_max[i] = val
        
        for i in range(len(nums)):
            if left_min[i] < nums[i] < right_max[i]:
                return True

        return False
