class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx: int, sub: list):
            if idx == len(nums):
                res.add(tuple(sub))
                return
            
            for i in range(idx, len(nums)):
                dfs(i+1, sub)
                sub.append(nums[i])
                dfs(i+1, sub)
                sub.pop()
        
        res = set()

        dfs(0, [])

        return list(res)
