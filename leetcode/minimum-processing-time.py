class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        res = 0
        tasks.sort()
        processorTime.sort(reverse=True)
        for i in range(len(processorTime)):
            res = max(res, tasks[(i+1)*4-1]+processorTime[i])
        return res
