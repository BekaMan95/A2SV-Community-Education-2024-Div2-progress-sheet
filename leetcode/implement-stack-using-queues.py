class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        return self.que.pop()

    def top(self) -> int:
        return self.que[-1]

    def empty(self) -> bool:
        return len(self.que) == 0
