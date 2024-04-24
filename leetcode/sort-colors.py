class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count, sorted_nums = Counter(nums), []
        for num in sorted(count.keys()):
            sorted_nums += [num]*count[num]
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]
        """
        Do not return anything, modify nums in-place instead.
        """
        
