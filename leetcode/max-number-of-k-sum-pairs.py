class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, ops = 0, len(nums)-1, 0
        while left < right:
            if nums[left] + nums[right] == k:
                ops += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return ops
