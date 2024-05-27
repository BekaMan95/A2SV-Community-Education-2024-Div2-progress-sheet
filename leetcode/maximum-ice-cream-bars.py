class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        res = 0
        while costs and coins:
            if coins >= costs[-1]:
                res += 1
                coins -= costs.pop()
            else:
                break
        return res
