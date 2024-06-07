class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res, idx, binary = 0, 0, [0]*len(flips)
        for i in range(len(flips)):
            binary[flips[i]-1] = 1
            while idx < len(flips) and binary[idx]:
                idx += 1
            if idx == i+1:
                res += 1
        return res
