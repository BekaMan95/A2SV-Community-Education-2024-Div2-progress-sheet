class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        values = [0]*50
        for x, y in ranges:
            for i in range(x-1, y):
                values[i] = 1
        for i in range(left-1, right):
            if not values[i]:
                return False
        return True
