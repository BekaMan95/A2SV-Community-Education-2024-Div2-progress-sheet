class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [(29, -1)], [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack: res[i] = stack[-1][1] - i
            else: res[i] = 0
            stack.append((temperatures[i], i))            

        return res
