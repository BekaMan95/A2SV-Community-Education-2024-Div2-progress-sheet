class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, res, count = 0, 0, defaultdict(int)
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if not count[fruits[l]]:
                    del count[fruits[l]]
                l += 1
            res = max(res, r-l+1)
        return res
