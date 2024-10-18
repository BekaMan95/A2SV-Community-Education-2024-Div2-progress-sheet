class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        nums = list()
        arr.sort(reverse=True)
        
        while arr:
            cur = arr.pop()
            if not nums:
                nums.append(1)
            elif abs(cur - nums[-1]) <= 1:
                nums.append(cur)
            else:
                nums.append(nums[-1] + 1)
            
        return max(nums)
