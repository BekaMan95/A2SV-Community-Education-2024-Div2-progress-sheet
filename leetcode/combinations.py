class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(cur: int, comb: list):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for nxt in range(cur+1, n+1):
                comb.append(nxt)
                backtrack(nxt, comb)
                comb.pop()
            
        res = list()
        
        backtrack(0, [])

        return res
