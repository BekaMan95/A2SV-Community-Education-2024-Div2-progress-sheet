class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l, min_len, count = 0, len(cards)+1, defaultdict(int)
        for r in range(len(cards)):
            count[cards[r]] += 1
            while count[cards[r]] >= 2:
                if cards[l] == cards[r] and count[cards[r]] == 2:
                    break
                count[cards[l]] -= 1
                l += 1
            if count[cards[r]] == 2:
                min_len = min(min_len, r-l+1)
        return min_len if min_len <= len(cards) else -1
