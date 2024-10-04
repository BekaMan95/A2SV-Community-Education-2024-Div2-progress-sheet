class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res, stack, mod = 0, list(), 10**9 + 7
        
        for i, num in enumerate(arr):
            while stack and num < stack[-1][0]:
                val, idx = stack.pop()
                l = idx - stack[-1][1] if stack else idx + 1
                r = i - idx
                res = (res + val * l * r) % mod
            stack.append((num, i))
        
        if stack:
            for i, pair in enumerate(stack):
                num, idx = pair
                l = idx - stack[i-1][1] if i else idx + 1
                r = len(arr) - idx
                res = (res + num * l * r) % mod

        return res % mod
