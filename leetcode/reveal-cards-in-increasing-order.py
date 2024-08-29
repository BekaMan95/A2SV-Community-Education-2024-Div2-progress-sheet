class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        out = [0] * len(deck)
        deck.sort(reverse=True)
        que = deque([i for i in range(len(deck))])
        while deck:
            out[que.popleft()] = deck.pop()
            if que: que.append(que.popleft())
        return out
