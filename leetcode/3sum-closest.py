class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        out = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                out.add(nums[i] + nums[l] + nums[r])
                if nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        out = sorted(out, key=lambda x:abs(x-target))
        return out[0]
