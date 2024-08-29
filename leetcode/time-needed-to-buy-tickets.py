class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res, que = 0, deque(tickets)
        while que:
            if k == 0 and que[k] == 1:
                res += 1
                break
            if que[0] > 1: que.append(que.popleft()-1)
            else: que.popleft()
            if not k: k = len(que)-1
            else: k -= 1
            res += 1
        return res
