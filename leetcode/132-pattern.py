class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, min_val, minStack = list(), float('inf'), list()

        for i, num in enumerate(nums):
            while stack and num > stack[-1]:
                stack.pop()
                minStack.pop()
            if i > 1 and stack and minStack[-1] < num < stack[-1]:
                return True
            stack.append(num)
            min_val = min(min_val, num)
            minStack.append(min_val)

        return False
