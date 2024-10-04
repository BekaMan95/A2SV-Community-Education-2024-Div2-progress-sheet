class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res, stack = [-1] * len(nums) * 2, [-10**9-1]
        nums += nums
        
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if not stack: res[i] = -1
            else: res[i] = stack[-1]
            stack.append(nums[i])
        
        return res[:len(nums) // 2]
