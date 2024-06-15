class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cache = [num for num in nums if num]
        for i in range(len(nums)):
            if i < len(cache):
                nums[i] = cache[i]
            else:
                nums[i] = 0
        """
        Do not return anything, modify nums in-place instead.
        """
        
