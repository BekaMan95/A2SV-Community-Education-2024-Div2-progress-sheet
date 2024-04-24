class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = []
        count = Counter(arr1)
        for num in arr2:
            out += [num]*count[num]
            count[num] = 0
        for num in sorted(count.keys()):
            if count[num]:
                out += [num]*count[num]
        return out
