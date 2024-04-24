class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        order = {}
        cache = sorted(nums)
        while cache:
            if len(cache) > 1 and cache[-2] == cache[-1]:
                cache.pop()
            else:
                order[cache.pop()] = len(cache)-1
        for i in range(len(nums)):
            nums[i] = order[nums[i]]
        return nums
