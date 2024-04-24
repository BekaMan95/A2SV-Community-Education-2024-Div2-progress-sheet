class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_width = 0
        for i in range(len(points)-1):
            max_width = max(max_width, points[i+1][0]-points[i][0])
        return max_width
