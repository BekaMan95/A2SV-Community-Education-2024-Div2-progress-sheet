class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        piles.pop()
        for i in range(int(len(piles)/3)+1):
            res += piles.pop()
            piles.pop()
        return res
