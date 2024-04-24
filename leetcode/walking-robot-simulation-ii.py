class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tot_steps = 0

    def step(self, num: int) -> None:
        # num = num % (((self.width + self.height)*2)-4)
        self.tot_steps += num

    def getPos(self) -> List[int]:
        idx = self.tot_steps % (((self.width + self.height)*2)-4)
        if idx < self.width:
            x = idx
            y = 0
        elif self.width <= idx < self.width+self.height-1:
            x = self.width-1
            y = idx - self.width + 1
        elif self.width+self.height-1 <= idx < 2*(self.width-1)+self.height-1:
            x = (2*(self.width-1)+self.height-1) - idx
            y = self.height-1
        else:
            x = 0
            if idx:
                y = (2*(self.width-1)+2*(self.height-1)) - idx
            else:
                y = 0

        return [x, y]

    def getDir(self) -> str:
        if not self.tot_steps:
            return 'East'
        idx = self.tot_steps % (((self.width + self.height)*2)-4)
        if 1 <= idx < self.width:
             return 'East'
        elif self.width <= idx < self.width+self.height-1:
            return 'North'
        elif self.width+self.height-1 <= idx < 2*(self.width-1)+self.height:
            return 'West'
        else:
            return 'South'


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
