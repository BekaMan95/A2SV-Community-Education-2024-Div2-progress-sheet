class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        l, res = 0, 0
        tot_sum, pfx = sum(cardPoints), sum(cardPoints[:n-k-1])
        for r in range(n-k-1, n):
            pfx += cardPoints[r]
            res = max(res, tot_sum - pfx)
            pfx -= cardPoints[l]
            l += 1
        return res
