class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                if not nums[i] + nums[l] + nums[r]:
                    out.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return out
