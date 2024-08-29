class RecentCounter:

    def __init__(self):
        self.que = deque()

    def ping(self, t: int) -> int:
        self.que.append(t)
        while t - self.que[0] > 3000:
            self.que.popleft()
        return len(self.que)
