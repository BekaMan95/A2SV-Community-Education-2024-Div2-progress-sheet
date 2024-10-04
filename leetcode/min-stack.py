class MinStack:

    def __init__(self):
        self.stack = list()
        self.MIN = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.MIN: self.MIN.append(min(val, self.MIN[-1]))
        else: self.MIN.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MIN.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MIN[-1]
