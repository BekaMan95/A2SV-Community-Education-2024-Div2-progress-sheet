class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for _, n in sorted([-heights[i], names[i]] for i in range(len(names)))]
