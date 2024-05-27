class Solution:
    def smallestNumber(self, num: int) -> int:
        val = list(str(num))
        if num < 0:
            val = val[1:]
            val.sort(reverse=True)
            return -int(''.join(val))
        elif num > 0:
            zeros = val.count('0')
            val = [c for c in val if c != '0']
            val.sort()
            return int(val[0]+('0'*zeros)+''.join(val[1:]))
        else:
            return num
